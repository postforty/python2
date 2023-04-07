# 지도에 마커 표시 하기 테스트
# pip install folium
import folium

map = folium.Map(location=[35.152417295, 129.059590906], zoom_start=7) # 0 ~ 18

marker = folium.Marker([35.152417295, 129.059590906], popup='코리아 IT 아카데미', icon=folium.Icon(color='blue'))

marker.add_to(map)

map.save('uni_map.html')