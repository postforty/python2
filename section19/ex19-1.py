import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = r'C:\Windows\Fonts\batang.ttc'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
# x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
x = ['1월', '2월', '3월', '4월', '5월', '6월']
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle="--", marker='^')
plt.show()