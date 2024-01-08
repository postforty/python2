import pandas as pd
import folium

path = '학교주소좌표.xlsx'
df_excel = pd.read_excel(path, engine='openpyxl', header=None)

df_excel.columns = ['학교명', '주소', 'x', 'y']

name_list = df_excel['학교명'].to_list()
address_list = df_excel['주소'].to_list()
position_x_list = df_excel['x'].to_list()
position_y_list = df_excel['y'].to_list()

map = folium.Map(location=[37, 127], zoom_start=7)

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i], position_x_list[i]], popup=name_list[i], icon=folium.Icon(color='blue'))
        marker.add_to(map)

map.save('uni_map.html')