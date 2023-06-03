import wordcloud
import matplotlib.pyplot as plt

words = {"파이썬": 10, "크롤링": 5, "빅데이터": 7, "인공지능": 9, "딥러닝": 12}
wc = wordcloud.WordCloud(font_path=r"C:\Windows\Fonts\HYGPRM.TTF")
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()
