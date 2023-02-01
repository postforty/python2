# pip install gtts
from gtts import gTTS

text = "안녕하세요."

tts = gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")

