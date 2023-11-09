# pip install wordcloud
import wordcloud
import matplotlib.pyplot as plt
words = {
    'Python': 100,
    'Java': 50,
    'C': 70,
    'C++': 90,
    'JSP': 120
}
wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()
