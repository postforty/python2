# https://www.vworld.kr/dev/v4api.do
# Geocoder API

# CABC17B4-3089-3C88-8FD5-4BEB23099EDE

# 주소를 좌표로 변환하는 코드
import requests

# apiurl = "http://api.vworld.kr/req/address?"
# params = {
#     "service": "address",
#     "request": "getcoord",
#     "crs": "epsg:4326",
#     "address": "판교로 242",
#     "format": "json",
#     "type": "road",
#     "key": "CABC17B4-3089-3C88-8FD5-4BEB23099EDE"
# }
# response = requests.get(apiurl, params=params)

# print("상태 코드 : ", response.status_code)

# import json

# if response.status_code == 200:
#     # print(response.json())
#     print(json.dumps(response.json(), indent='\t') )

def request_geo(road):
    apiurl = "http://api.vworld.kr/req/address?"
    params = {
        "service": "address",
        "request": "getcoord",
        "crs": "epsg:4326",
        "address": road,
        "format": "json",
        "type": "road",
        "key": "CABC17B4-3089-3C88-8FD5-4BEB23099EDE"
    }

    response = requests.get(apiurl, params=params)
    json_data = response.json()

    # print(json_data)

    # return(json_data)
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        x = 0
        y = 0
        return x, y

# print(request_geo("판교로 242"))

x, y = request_geo("부산광역시 부산진구 중앙대로 668") # unpacking

print(f'경도: {x}')
print(f'위도: {y}')