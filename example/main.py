# main.py
import requests

try:
    response = requests.get("https://www.naver.com")
    print(f"요청 성공! 상태 코드: {response.status_code}")
    response.raise_for_status() # 200 OK가 아니면 예외 발생
except requests.exceptions.RequestException as e:
    print(f"요청 중 오류 발생: {e}")