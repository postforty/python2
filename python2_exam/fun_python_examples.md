# 흥미로운 Python 미니 프로젝트 예제

기초 문법을 넘어, 외부 라이브러리를 활용하거나 시각적인 결과물을 만들어낼 수 있는 흥미로운 예제들입니다.

## 1. 나만의 QR 코드 생성기
- **설명**: 원하는 인터넷 주소(URL)나 텍스트를 QR 코드로 변환하여 이미지 파일로 저장합니다.
- **필요 라이브러리**: `qrcode`, `pillow`
- **학습 포인트**: 외부 라이브러리 설치(`pip install`) 및 사용법, 이미지 저장.
```python
import qrcode

img = qrcode.make('https://www.google.com')
img.save('google_qr.png')
```

## 2. 텍스트를 음성으로 변환 (Text-to-Speech)
- **설명**: 내가 입력한 글자를 컴퓨터가 읽어주는 MP3 파일을 만듭니다.
- **필요 라이브러리**: `gTTS` (Google Text-to-Speech)
- **학습 포인트**: API 활용, 파일 저장 및 재생.
```python
from gtts import gTTS

text = "안녕하세요, 파이썬은 정말 재미있어요!"
tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")
```

## 3. 거북이 경주 게임 (Turtle Graphics)
- **설명**: 파이썬 내장 라이브러리인 `turtle`을 사용하여 여러 마리의 거북이가 달리기 경주를 하는 게임을 만듭니다.
- **필요 라이브러리**: `turtle`, `random` (내장 모듈)
- **학습 포인트**: 그래픽 프로그래밍 기초, 좌표계 이해, 랜덤 이동.

## 4. 데스크탑 알림 보내기
- **설명**: 윈도우 우측 하단에 알림 메시지를 띄웁니다. (예: "물 마실 시간입니다!", "스트레칭 하세요!")
- **필요 라이브러리**: `plyer`
- **학습 포인트**: 시스템 알림 제어, 스케줄링(일정 시간마다 알림).
```python
from plyer import notification

notification.notify(
    title='휴식 알림',
    message='잠시 쉬었다 하세요!',
    app_name='Python App',
    timeout=10
)
```

## 5. ASCII 아트 생성기
- **설명**: 일반 텍스트를 멋진 ASCII 아트(특수문자로 만든 글자)로 변환해줍니다.
- **필요 라이브러리**: `art`
- **학습 포인트**: 문자열 처리, 외부 모듈 활용.
```python
from art import tprint
tprint("PYTHON")
```

## 6. 환율 계산기 (GUI)
- **설명**: `tkinter`를 사용하여 창을 띄우고, 원화를 입력하면 달러/엔화 등으로 변환해줍니다.
- **필요 라이브러리**: `tkinter` (내장), `requests` (실시간 환율 정보 가져오기 심화)
- **학습 포인트**: GUI 프로그래밍, 이벤트 처리(버튼 클릭).

## 7. 유튜브 영상 다운로더
- **설명**: 유튜브 링크를 입력하면 영상을 다운로드합니다.
- **필요 라이브러리**: `yt-dlp`
- **학습 포인트**: 멀티미디어 처리, 라이브러리 활용.
