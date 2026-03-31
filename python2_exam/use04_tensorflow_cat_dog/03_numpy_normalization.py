import numpy as np
from PIL import Image, ImageOps

# 1. 넘파이 배열 기초 연습
# (1) 0으로 가득 찬 3x3 배열을 만들어 봅니다.
print("--- 3x3 빈 배열 생성 ---")
arr = np.zeros((3, 3))
print(arr)

# 2. 이미지 데이터 전처리 실습 (PIL)
# (1) 임의의 이미지를 생성하거나 로드하여 RGB로 변환합니다.
# 실습을 위해 400x300 크기의 검은색 이미지를 생성합니다.
print("\n--- 이미지 로드 및 전처리 연습 ---")
# image = Image.new("RGB", (400, 300), color=(0, 0, 0)) # Image.open("img.jpg").convert("RGB")와 동일 효과
image = Image.open("images/cat_2.jpg").convert("RGB")
print(f"원본 이미지 크기: {image.size}")

# (2) 224x224 크기로 리사이징 및 중심 정렬 크롭 (ImageOps.fit)
# AI 모델은 정해진 크기(예: 224x224)의 입력을 요구하는 경우가 많습니다.
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
print(f"전처리 후 이미지 크기: {image.size}")

# (3) 이미지를 넘파이 배열로 변환합니다.
image_array = np.asarray(image)
print(f"넘파이 배열 형태: {image_array.shape}") # (224, 224, 3) -> 높이, 너비, RGB 채널
print(f"넘파이 배열 형태: {image_array}")

# 3. 이미지 데이터 정규화 연습
# (1) 실제 픽셀 값(0~255) 대신 연습용 데이터를 사용합니다.
# data = np.array([0, 128, 255]) 
data = np.array(image_array[0, 0]) # 이미지의 첫 번째 픽셀(좌상단) RGB 값 예시
print(f"\n원본 데이터: {data}")

# (2) 이미지 전처리 공식 적용: (데이터 / 127.5) - 1
# AI 모델은 -1.0 ~ 1.0 사잇값을 좋아하므로 정규화합니다.
normalized_data = (data.astype(np.float32) / 127.5) - 1
print(f"정규화 데이터: {normalized_data}")
# 0 -> -1.0, 128 -> 약 0.003, 255 -> 1.0 으로 변환됨을 확인할 수 있습니다.

# (3) 가장 높은 값(확률) 찾기 (np.argmax)
# [고양이 확률, 강아지 확률] 순서라고 가정할 때:
predictions = [0.12, 0.88] # 확률 데이터
index = np.argmax(predictions) # 가장 큰 값의 인덱스(번호) 반환
print(f"\n예측 확률 리스트: {predictions}")
print(f"가장 높은 확률을 가진 인덱스: {index}") # 1(강아지)이 나옵니다.
