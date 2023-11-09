from matplotlib import font_manager, rc 
import matplotlib.pyplot as plt
font_path = r'C:\Windows\Fonts\batang.ttc'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
x = ['봄', '여름', '가을', '겨울']
y = [20.5, 30.5, 15.5, 1.5]
axes.plot(x, y)
plt.show()