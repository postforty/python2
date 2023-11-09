import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
x1 = [0, 1, 2, 3, 4]
y1 = [0, 3, 0, 3, 0]
x2 = [0, 1, 2, 3, 4]
y2 = [1, 2, 3, 4, 5]
axes.plot(x1, y1, linestyle=':', linewidth=5.0)
axes.plot(x2, y2, color='g', marker='^')
plt.show()