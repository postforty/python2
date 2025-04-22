import socket
import threading
import sys

# 서버 정보
SERVER_IP = '127.0.0.1' # 서버 IP 주소 (서버와 동일한 머신이면 127.0.0.1)
SERVER_PORT = 9999       # 서버 포트 번호
BUFFER_SIZE = 1024       # 메시지 수신 버퍼 크기

# 서버로부터 메시지를 수신하는 함수 (스레드에서 실행됨)
def receive_messages(client_socket):
    while True:
        try:
            message_bytes = client_socket.recv(BUFFER_SIZE)
            if not message_bytes:
                print("[연결 종료] 서버와의 연결이 끊겼습니다.")
                break # 서버 연결 끊김

            message_str = message_bytes.decode('utf-8')
            print(message_str) # 수신 메시지 출력

        except ConnectionAbortedError:
             print("[연결 오류] 현재 연결이 중단되었습니다.")
             break
        except ConnectionResetError:
             print("[연결 오류] 서버와의 연결이 초기화되었습니다.")
             break
        except Exception as e:
            print(f"[수신 오류] 메시지 수신 중 오류 발생: {e}")
            break # 오류 발생 시 루프 종료

    print("수신 스레드를 종료합니다.")
    client_socket.close() # 소켓 닫기

# 사용자 입력을 받아 서버로 메시지를 전송하는 함수
def send_messages(client_socket):
    try:
        while True:
            message = input() # 사용자 입력 대기
            if message.lower() == 'exit': # 'exit' 입력 시 종료
                break
            if message: # 빈 메시지가 아니면 전송
                client_socket.send(message.encode('utf-8'))

    except EOFError: # Ctrl+D (Unix) 또는 Ctrl+Z+Enter (Windows) 입력 시
        print("입력이 종료되었습니다.")
    except Exception as e:
        print(f"[송신 오류] 메시지 전송 중 오류 발생: {e}")
    finally:
        # 종료 의사를 서버에 알리거나 소켓을 닫는 로직 추가 가능
        print("송신 입력을 종료합니다. 프로그램을 닫으려면 Enter를 누르세요.")
        # receive 스레드가 종료될 수 있도록 소켓을 닫아 recv()에서 예외 발생 유도
        client_socket.close()


# 클라이언트 시작 함수
def start_client():
    # TCP 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 서버에 연결 시도
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"[연결 성공] 서버({SERVER_IP}:{SERVER_PORT})에 연결되었습니다.")
        print("채팅을 시작합니다. 종료하려면 'exit'를 입력하세요.")

        # 메시지 수신을 위한 스레드 생성 및 시작
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True # 메인 스레드 종료 시 함께 종료
        receive_thread.start()

        # 메인 스레드에서는 메시지 송신 처리
        send_messages(client_socket)

    except ConnectionRefusedError:
        print("[연결 실패] 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
    except Exception as e:
        print(f"[오류] 클라이언트 실행 중 오류 발생: {e}")
    finally:
        # 프로그램 종료 전 최종 소켓 닫기 (이미 닫혔을 수 있음)
        if client_socket.fileno() != -1 : # 소켓이 유효한지 확인
             client_socket.close()
        print("[클라이언트 종료]")
        # 수신 스레드가 완전히 종료될 때까지 잠시 대기 (선택 사항)
        # receive_thread.join()

# 메인 실행 부분
if __name__ == "__main__":
    start_client()