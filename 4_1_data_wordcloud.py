# pip install wordcloud
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
# 설치 에러 발생시 위 주소에서 파이썬 버전에 맞는 whl 파일 다운로드 및 pip install 진행
import wordcloud
import matplotlib.pyplot as plt
words = {
    'Python':10,
    'Java': 5,
    'C': 7,
    'C++': 9,
    'JSP': 12
}
wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()