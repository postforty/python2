# pip install wordcloud
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
# 설치 에러 발생시 위 주소에서 파이썬 버전에 맞는 whl 파일 다운로드 및 pip install 진행
import wordcloud
import matplotlib.pyplot as plt
words = {
    '파이썬':10,
    '크롤링': 5,
    '빅데이터': 7,
    '인공지능': 9,
    '딥러닝': 12
}
wc = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\HYGPRM.TTF')
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()