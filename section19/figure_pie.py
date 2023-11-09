import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
data = [1, 2, 3]
label = ['Good', 'Bad', 'Normal']
axes.pie(data, labels=label, autopct='%0.2f%%')
plt.axis('equal')
plt.legend(label, loc="lower right")

plt.show()