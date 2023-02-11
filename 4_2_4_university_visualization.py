# 지도에 마커 표시 하기 테스트
# pip install folium
import folium

map = folium.Map(location=[35.232846735, 129.074661279], zoom_start=7) # 0 ~ 18

marker = folium.Marker([35.232846735, 129.074661279], popup='부산대학교', icon=folium.Icon(color='blue'))

marker.add_to(map)

map.save('uni_map.html')