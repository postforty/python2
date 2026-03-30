import os
import glob
import shutil
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# 경로 설정
PATH = os.path.dirname(__file__)
IMG_DIR = os.path.join(PATH, "images")
RESULT_DIR = os.path.join(PATH, "result")

# 결과 폴더(cat, dog) 생성
for label in ["cat", "dog"]:
    os.makedirs(os.path.join(RESULT_DIR, label), exist_ok=True)

# 모델 및 레이블 로드
model = load_model(os.path.join(PATH, "keras_model.h5"), compile=False)
with open(os.path.join(PATH, "labels.txt"), "r") as f:
    class_names = f.readlines()

# 데이터 처리를 위한 설정 (Teachable Machine 규격: 224x224 RGB)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# 'images' 폴더 내의 이미지 파일 검색 (*.jpg, *.jpeg, *.png)
image_files = []
for ext in ("*.jpg", "*.jpeg", "*.png"):
    image_files.extend(glob.glob(os.path.join(IMG_DIR, ext)))

if not image_files:
    print(f"'{IMG_DIR}' 폴더 내에 이미지 파일이 존재하지 않습니다.")
else:
    print(f"총 {len(image_files)}개의 이미지를 분류하기 시작합니다...")
    
    for img_path in image_files:
        try:
            # 1. 이미지 로드 및 전처리
            file_name = os.path.basename(img_path)
            image = Image.open(img_path).convert("RGB")
            
            # 224x224 크기로 리사이징 및 중심 정렬 크롭
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            
            # 넘파이 배열로 변환 및 정규화
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
            data[0] = normalized_image_array
            
            # 2. 모델 예측
            prediction = model.predict(data)
            index = np.argmax(prediction)
            
            # labels.txt 구조가 "0 cat" 형태이므로 공백으로 나누어 이름만 추출
            label_name = class_names[index].strip().split()[1]
            confidence_score = prediction[0][index]
            
            # 3. 결과 폴더로 이미지 복사
            dest_path = os.path.join(RESULT_DIR, label_name, file_name)
            shutil.copy(img_path, dest_path)
            
            print(f"[분류 완료] {file_name} -> {label_name} (신뢰도: {confidence_score:.2f})")
            
        except Exception as e:
            print(f"[에러 발생] {file_name}: {e}")

print("\n--- 모든 이미지 분류 및 정리가 완료되었습니다. ---")

