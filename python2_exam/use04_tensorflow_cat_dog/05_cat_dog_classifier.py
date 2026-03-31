# uv add tensorflow-cpu tf-keras pillow numpy

import os
import glob
import shutil

# 1. Keras 2 호환 엔진 설정 (최상단 배치)
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import tensorflow as tf
import tf_keras as keras  # uv add tf-keras 필요
from tf_keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# 경로 설정 (절대 경로 확보)
PATH = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(PATH, "images")
RESULT_DIR = os.path.join(PATH, "result")

# 모델 및 레이블 로드
MODEL_PATH = os.path.join(PATH, "keras_model.h5")
LABEL_PATH = os.path.join(PATH, "labels.txt")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")

# 모델 로드
model = load_model(MODEL_PATH, compile=False)

# 레이블 로드 및 처리
with open(LABEL_PATH, "r", encoding="utf-8") as f:
    # "0 cat\n" -> "cat" 형태로 깔끔하게 리스트화
    class_names = [line.strip().split()[-1].lower() for line in f.readlines()]

# 결과 폴더(레이블별) 생성
for label in class_names:
    os.makedirs(os.path.join(RESULT_DIR, label), exist_ok=True)

# 데이터 처리를 위한 설정 (Teachable Machine 규격: 224x224 RGB)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# 이미지 파일 검색 (대소문자 무시를 위해 리스트 확장)
extensions = ["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"]
image_files = []
for ext in extensions:
    image_files.extend(glob.glob(os.path.join(IMG_DIR, f"*.{ext}")))

if not image_files:
    print(f"'{IMG_DIR}' 폴더 내에 분류할 이미지 파일이 없습니다.")
else:
    print(f"총 {len(image_files)}개의 이미지를 분류하기 시작합니다...\n")
    
    for img_path in image_files:
        file_name = os.path.basename(img_path)
        try:
            # 1. 이미지 로드 및 전처리
            image = Image.open(img_path).convert("RGB")
            
            # 224x224 크기로 리사이징 및 중심 정렬 크롭
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            
            # 넘파이 배열로 변환 및 정규화
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
            data[0] = normalized_image_array
            
            # 2. 모델 예측 (verbose=0으로 로그 출력 억제)
            prediction = model.predict(data, verbose=0)
            index = np.argmax(prediction)
            
            label_name = class_names[index]
            confidence_score = prediction[0][index]
            
            # 3. 결과 폴더로 이미지 복사 (shutil.copy2는 메타데이터까지 보존)
            dest_dir = os.path.join(RESULT_DIR, label_name)
            os.makedirs(dest_dir, exist_ok=True) # 안전장치
            
            dest_path = os.path.join(dest_dir, file_name)
            shutil.copy2(img_path, dest_path)
            
            print(f"[✅ 완료] {file_name:20} -> {label_name:5} (신뢰도: {confidence_score:.2f})")
            
        except Exception as e:
            print(f"[❌ 에러] {file_name}: {e}")

print("\n" + "="*50)
print("모든 이미지 분류 및 정리가 완료되었습니다.")
print(f"결과 확인: {RESULT_DIR}")
print("="*50)