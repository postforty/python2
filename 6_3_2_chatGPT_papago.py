# https://developers.naver.com/docs/papago/papago-nmt-example-code.md#python

import os
import sys
import urllib.request

import json #TODO

client_id = "c3RaOpS5Ymkf7kgPMLgt" # 개발자센터에서 발급받은 Client ID 값
client_secret = "CQthN1Y7xi" # 개발자센터에서 발급받은 Client Secret 값

# 한글 > 영어
encText = urllib.parse.quote("반갑습니다")
data = ("source=ko&target=en&text=" + encText).encode("utf-8")
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    # TODO
    msg = response_body.decode('utf-8')
    jsonObject = json.loads(msg)
    print(jsonObject.get("message").get("result").get('translatedText'))
    # print(msg)
else:
    print("Error Code:" + rescode)

# 영어 > 한글
encText = urllib.parse.quote("Nice to meet you.")
data = ("source=en&target=ko&text=" + encText).encode("utf-8")
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    # TODO
    msg = response_body.decode('utf-8')
    jsonObject = json.loads(msg)
    print(jsonObject.get("message").get("result").get('translatedText'))
    # print(msg)
else:
    print("Error Code:" + rescode)