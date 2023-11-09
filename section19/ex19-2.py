from matplotlib import font_manager, rc 
import matplotlib.pyplot as plt

font_path = r'C:\Windows\Fonts\batang.ttc'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
noise = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
stress = [10, 11, 15, 20, 30, 42, 55, 70, 88, 110, 150]
axes.scatter(noise, stress, s=50)
plt.title('소음에 따른 스트레스 지수')
plt.xlabel('소음')
plt.ylabel('스트레스')
plt.show()