# server.py (종료 로직 개선)
import socket  # 소켓 통신을 위한 라이브러리
import threading  # 멀티쓰레딩을 위한 라이브러리
import time  # time.sleep 사용 위해 추가 (서버 종료 시 클라이언트에게 메시지 전송을 위한 대기 시간 확보)

# 서버 설정
HOST = '0.0.0.0'  # 모든 IP 주소에서 접속 허용
PORT = 9999  # 사용할 포트 번호
MAX_CLIENTS = 10  # 최대 클라이언트 수

# 연결된 클라이언트 소켓 목록 및 정보
client_sockets = []  # 연결된 클라이언트 소켓을 저장하는 리스트
clients_info = {}  # 클라이언트 소켓과 주소를 매핑하는 딕셔너리
lock = threading.Lock()  # 쓰레드 간의 동기화를 위한 Lock 객체
server_running = True  # 서버 실행 상태 플래그 추가 (서버 종료를 제어하기 위해)

# --- broadcast, remove_client, handle_client 함수는 이전과 동일하게 유지 ---
# 모든 클라이언트에게 메시지 브로드캐스트하는 함수


def broadcast(message_bytes, sender_socket=None):
    """
    특정 클라이언트(sender_socket)를 제외한 모든 클라이언트에게 메시지를 전송합니다.
    """
    with lock:  # Lock을 사용하여 쓰레드 안전성을 확보
        current_clients = client_sockets[:]  # 클라이언트 목록 복사 (순회 중 변경 방지)
        for client_socket in current_clients:  # 모든 클라이언트 소켓에 대해 반복
            if client_socket != sender_socket:  # 메시지 발신자를 제외
                try:
                    client_socket.sendall(message_bytes)  # 메시지 전송
                except Exception as e:
                    print(
                        f"[오류] 브로드캐스트 중 오류 발생 ({clients_info.get(client_socket, '알수없음')}): {e}")
                    remove_client(client_socket)  # 오류 발생 시 클라이언트 제거

# 클라이언트 연결 해제 처리 함수


def remove_client(client_socket):
    """
    클라이언트 소켓을 목록에서 제거하고 연결을 종료합니다.
    """
    with lock:  # Lock을 사용하여 쓰레드 안전성을 확보
        if client_socket in client_sockets:  # 클라이언트 소켓이 목록에 있는지 확인
            address = clients_info.get(client_socket)  # 클라이언트 주소 가져오기
            print(f"[연결 종료] {address} 연결 해제 시도")
            client_sockets.remove(client_socket)  # 클라이언트 소켓 제거
            if client_socket in clients_info:  # 클라이언트 정보가 있는지 확인
                del clients_info[client_socket]  # 클라이언트 정보 제거
            try:
                client_socket.close()  # 소켓 닫기
                print(f"[연결 종료] {address} 소켓 닫힘")
            except Exception as e:
                print(f"[오류] 소켓 닫기 중 오류 발생 ({address}): {e}")

            # 사용자 퇴장 메시지 브로드캐스트 (서버 종료 시에는 별도 메시지 전송)
            # 서버 종료가 아닐 경우에만 퇴장 메시지 전송하도록 조건 추가 가능
            global server_running
            if server_running and address:  # 서버가 정상 실행 중일 때만 퇴장 메시지 전송
                exit_message = f"알림: {address} 님이 퇴장하셨습니다.".encode('utf-8')
                broadcast(exit_message)  # 퇴장 메시지 브로드캐스트

# 개별 클라이언트 처리 함수


def handle_client(client_socket, address):
    """
    개별 클라이언트와의 연결을 처리하는 함수입니다.
    클라이언트로부터 메시지를 수신하고, 다른 클라이언트들에게 브로드캐스트합니다.
    """
    print(f"[새 연결] {address} 연결됨")
    with lock:  # Lock을 사용하여 쓰레드 안전성을 확보
        client_sockets.append(client_socket)  # 클라이언트 소켓 목록에 추가
        clients_info[client_socket] = address  # 클라이언트 정보 딕셔너리에 추가

    entry_message = f"알림: {address} 님이 입장하셨습니다.".encode('utf-8')
    broadcast(entry_message, client_socket)  # 입장 메시지 브로드캐스트

    try:
        while True:  # 클라이언트로부터 메시지를 계속 수신
            # 서버 종료 신호 확인 (선택적)
            # global server_running
            # if not server_running:
            #     break

            message_bytes = client_socket.recv(
                1024)  # 클라이언트로부터 메시지 수신 (최대 1024 바이트)
            if not message_bytes:  # 메시지가 없으면 연결 종료
                print(f"[메시지 없음] {address} 로부터 빈 메시지 수신, 연결 종료 처리")
                break

            message_str = message_bytes.decode('utf-8')  # 수신된 메시지를 UTF-8로 디코딩
            print(f"[{address}] {message_str}")  # 메시지 출력

            full_message_bytes = f"[{address}] {message_str}".encode(
                'utf-8')  # 전체 메시지 구성 후 UTF-8로 인코딩
            broadcast(full_message_bytes, client_socket)  # 메시지 브로드캐스트

    except ConnectionResetError:  # 연결 재설정 오류 처리
        print(f"[연결 오류] {address} 와의 연결이 강제로 종료되었습니다.")
    except ConnectionAbortedError:  # 연결 중단 오류 처리
        print(f"[연결 오류] {address} 와의 연결이 중단되었습니다.")
    except OSError as e:  # 소켓이 닫힌 후 recv 시 발생 가능
        if e.errno == 9:  # Bad file descriptor (소켓이 이미 닫힘)
            print(f"[정보] {address} 소켓이 이미 닫혔습니다.")
        else:
            print(f"[오류] {address} 처리 중 OSError 발생: {e}")
    except Exception as e:  # 기타 예외 처리
        print(f"[오류] {address} 처리 중 예외 발생: {e}")
    finally:  # 예외 발생 여부와 관계없이 항상 실행
        print(f"[처리 종료] {address} 핸들러 종료, 제거 절차 시작")
        remove_client(client_socket)  # 클라이언트 제거

# 서버 종료 처리 함수 (신규 추가)


def shutdown_server(server_socket):
    """
    서버를 안전하게 종료하는 함수입니다.
    모든 클라이언트에게 종료 메시지를 보내고, 연결을 종료한 후 서버 소켓을 닫습니다.
    """
    global server_running
    server_running = False  # 서버 상태 변경 (종료 상태로 설정)

    print("\n[서버 종료] 서버 종료 절차를 시작합니다...")

    # 1. 모든 클라이언트에게 종료 메시지 전송
    shutdown_msg = "알림: 서버가 종료됩니다. 연결을 종료합니다.".encode('utf-8')  # 종료 메시지 생성
    print("[서버 종료] 클라이언트에게 종료 알림 전송 중...")
    broadcast(shutdown_msg)  # 종료 메시지 브로드캐스트
    time.sleep(0.5)  # 메시지 전송 위한 잠시 대기 (클라이언트가 메시지를 받을 시간을 확보)

    # 2. 모든 클라이언트 소켓 닫기
    print("[서버 종료] 모든 클라이언트 연결 종료 중...")
    with lock:  # Lock을 사용하여 쓰레드 안전성을 확보
        # 리스트 복사본 사용하여 순회 중 변경 문제 방지
        sockets_to_close = client_sockets[:]
        for cs in sockets_to_close:  # 모든 클라이언트 소켓에 대해 반복
            if cs in client_sockets:  # 아직 제거되지 않았다면 제거 및 닫기
                remove_client(cs)  # remove_client가 내부적으로 close 호출
            # 이미 remove_client에서 close 하므로 중복 호출 피함
            # try:
            #     cs.close()
            # except Exception as e_close:
            #     print(f"[오류] 종료 중 클라이언트 소켓({clients_info.get(cs)}) 닫기 오류: {e_close}")
    print(f"[서버 종료] 남은 클라이언트 수: {len(client_sockets)}")  # 확인용

    # 3. 서버 리스닝 소켓 닫기
    print("[서버 종료] 메인 서버 소켓 닫는 중...")
    try:
        server_socket.close()  # 서버 소켓 닫기
        print("[서버 종료] 메인 서버 소켓을 닫았습니다.")
    except Exception as e:  # 예외 처리
        print(f"[서버 오류] 메인 서버 소켓 닫기 중 오류 발생: {e}")

    print("[서버 종료] 서버가 완전히 종료되었습니다.")


# 서버 시작 함수 (수정됨)
def start_server():
    """
    서버를 시작하고 클라이언트 연결을 수락하는 함수입니다.
    """
    global server_running
    server_running = True  # 서버 시작 시 상태 True로 설정

    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # 서버 소켓 생성 (IPv4, TCP)
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 소켓 옵션 설정 (주소 재사용)

    # 타임아웃 설정: accept()에서 무한정 대기하지 않고 주기적으로 server_running 확인
    # 1초마다 타임아웃 (KeyboardInterrupt에 의한 종료를 더 잘 감지하기 위함)
    server_socket.settimeout(1.0)

    try:
        server_socket.bind((HOST, PORT))  # 서버 소켓에 주소 바인딩
        server_socket.listen(MAX_CLIENTS)  # 클라이언트 연결 대기 (최대 MAX_CLIENTS)
        print(f"[서버 시작] {HOST}:{PORT} 에서 연결 대기 중... (종료: Ctrl+C)")

        while server_running:  # server_running 플래그 확인 (서버 종료 조건)
            try:
                # 클라이언트 연결 수락 (타임아웃 설정됨)
                client_socket, address = server_socket.accept()  # 클라이언트 연결 수락

                # 새 클라이언트 처리를 위한 스레드 생성 및 시작
                client_thread = threading.Thread(
                    # 클라이언트 처리 스레드 생성
                    target=handle_client, args=(client_socket, address))
                client_thread.daemon = True  # 데몬 스레드로 설정 (메인 스레드 종료 시 함께 종료)
                client_thread.start()  # 스레드 시작

            except socket.timeout:  # 타임아웃 예외 처리
                # accept 타임아웃 발생 시 아무것도 하지 않고 루프 계속 (server_running 확인)
                continue
            except OSError as e:  # 소켓 오류 예외 처리
                # 서버 소켓이 닫힌 후 accept 시도 시 오류 발생 가능
                if server_running:  # 서버가 정상 종료 중이 아닐 때만 오류 로깅
                    print(f"[서버 오류] 소켓 accept 중 오류 발생: {e}")
                break  # 루프 종료
            except Exception as e:  # 기타 예외 처리
                if server_running:
                    print(f"[서버 오류] 예상치 못한 오류 발생: {e}")
                break  # 루프 종료

    except KeyboardInterrupt:  # Ctrl+C 입력 예외 처리
        print("\n[신호 감지] Ctrl+C 입력 감지. 서버 종료를 시작합니다.")
        # 여기서 shutdown_server 호출하지 않음. finally에서 처리.
    except Exception as e:  # 기타 예외 처리
        print(f"[서버 오류] 서버 실행 중 예외 발생: {e}")
    finally:  # 예외 발생 여부와 관계없이 항상 실행
        # 서버 종료 처리 함수 호출 (정상 종료든, 예외 발생이든)
        shutdown_server(server_socket)  # 서버 종료 함수 호출


# 메인 실행 부분
if __name__ == "__main__":
    start_server()  # 서버 시작
