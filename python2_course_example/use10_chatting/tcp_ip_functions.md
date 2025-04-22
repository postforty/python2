# server.py 코드에서 TCP/IP 4계층과 관련된 기능 정리

## 1. 애플리케이션 계층

- **데이터 인코딩/디코딩:**
  - `message_str = message_bytes.decode('utf-8')` (수신된 메시지 디코딩)
  - `full_message_bytes = f"[{address}] {message_str}".encode('utf-8')` (전체 메시지 인코딩)
  - 채팅 메시지를 UTF-8 형식으로 인코딩 및 디코딩하여 전송합니다.
- **메시지 브로드캐스팅:**
  - `broadcast(full_message_bytes, client_socket)`
  - 수신된 메시지를 다른 클라이언트들에게 전달합니다.

## 2. 전송 계층 (TCP)

- **소켓 생성 및 설정:**
  - `server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` (TCP 소켓 생성)
  - `server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` (소켓 옵션 설정)
  - TCP 소켓을 생성하고, 주소 재사용 옵션을 설정합니다.
- **연결 수립:**
  - `client_socket, address = server_socket.accept()` (클라이언트 연결 수락)
  - 클라이언트의 연결 요청을 수락하고, 클라이언트 소켓과 주소를 반환합니다.
- **데이터 송수신:**
  - `message_bytes = client_socket.recv(1024)` (데이터 수신)
  - `client_socket.sendall(message_bytes)` (데이터 전송)
  - 클라이언트로부터 데이터를 수신하고, 다른 클라이언트들에게 데이터를 전송합니다.
- **연결 종료:**
  - `client_socket.close()` (소켓 닫기)
  - 클라이언트와의 연결을 종료합니다.

## 3. 인터넷 계층 (IP)

- **IP 주소 설정:**
  - `HOST = '0.0.0.0'` (IP 주소 설정)
  - 서버가 모든 IP 주소에서 연결을 수락하도록 설정합니다.
- **포트 설정:**
  - `PORT = 9999` (포트 번호 설정)
  - 서버가 사용할 포트 번호를 설정합니다.
- **주소 바인딩:**
  - `server_socket.bind((HOST, PORT))` (주소 바인딩)
  - 서버 소켓에 IP 주소와 포트 번호를 할당합니다.

## 4. 링크 계층

- 해당 코드에서는 링크 계층과 직접적으로 관련된 기능은 없습니다. 링크 계층은 운영체제 및 네트워크 장비에서 처리되며, 소켓 통신을 위한 물리적인 연결을 제공합니다.

## 5. 추가 설명

- `threading.Lock()`: 쓰레드 간의 동기화를 위한 Lock 객체를 사용하여 공유 자원에 대한 접근을 제어합니다. 이는 TCP 연결 관리를 안전하게 수행하기 위해 필요합니다.
- `server_running`: 서버의 실행 상태를 제어하는 플래그입니다. 서버를 안전하게 종료하기 위해 사용됩니다.
- `socket.settimeout(1.0)`: `accept()` 함수에서 무한정 대기하는 것을 방지하고, 주기적으로 `server_running` 플래그를 확인합니다.
