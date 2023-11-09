import wordcloud
import matplotlib.pyplot as plt
words = {
    '파이썬': 100,
    '자바': 50,
    '씨': 70,
    '씨뿔뿔': 90,
    '제이에스피': 120
}
wc = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\batang.ttc')
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()
