import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [8, 6, 5, 4, 7, 9, 5]
axes.bar(x, y)
plt.title('weekday call')
plt.xlabel('week')
plt.ylabel('call')
plt.show()