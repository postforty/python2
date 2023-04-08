# https://codingspooning.tistory.com/entry/AI-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-GPT-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0#google_vignette

# https://keep-steady.tistory.com/m/51

import os
# pip install openai
import openai

openai.api_key = "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"

while True:
        question = input("Q: ")
        if question == '종료' or question == 'exit':
                break

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
        print('A:', response.choices[0].text.strip())