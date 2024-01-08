# https://codingspooning.tistory.com/entry/AI-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-GPT-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0#google_vignette

# https://keep-steady.tistory.com/m/51

import os
# pip install openai
import openai
import urllib.request
import json #TODO

openai.api_key = "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"

client_id = "c3RaOpS5Ymkf7kgPMLgt" # 개발자센터에서 발급받은 Client ID 값
client_secret = "CQthN1Y7xi" # 개발자센터에서 발급받은 Client Secret 값

while True:
        # 한글 > 영어
        encText = urllib.parse.quote(input("Q: "))
        data = ("source=ko&target=en&text=" + encText).encode("utf-8")
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data)
        rescode = response.getcode()

        question = ''

        if(rescode==200):
                response_body = response.read()
                # print(response_body.decode('utf-8'))
                # TODO
                msg = response_body.decode('utf-8')
                jsonObject = json.loads(msg)
                question = jsonObject.get("message").get("result").get('translatedText')
                # print(msg)
        else:
                print("Error Code:" + rescode)

        if question == '종료' or question == 'exit':
                break

        # print(question)

        response = (openai.Completion()).create(
                model="text-davinci-003",
                prompt=question,
                temperature=0,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                best_of=1,)

        # print(response)
        # print('A:', response.choices[0].text.strip())
        answer = response.choices[0].text.strip()

        # 영어 > 한글
        encText = urllib.parse.quote(answer)
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
                print('A:',jsonObject.get("message").get("result").get('translatedText'))
                # print(msg)
        else:
                print("Error Code:" + rescode)