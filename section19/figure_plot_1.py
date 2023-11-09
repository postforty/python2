import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
x1 = [0, 1, 2, 3, 4]
y1 = [4, 1, 3, 5, 2]
x2 = [0, 1, 2, 3, 4]
y2 = [0, 8, 5, 3, 1]
axes.plot(x1, y1)
axes.plot(x2, y2)
plt.show()