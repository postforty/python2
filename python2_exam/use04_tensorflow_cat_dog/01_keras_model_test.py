# 클래스당 최소 200~500장 이미지 확보 요망
# Teachable Machine: https://teachablemachine.withgoogle.com/
# uv venv --python 3.11
# uv add tensorflow==2.15.1
import os

# 1. Keras 2 엔진 사용을 위한 환경 변수 설정 (최상단 배치)
os.environ["TF_USE_LEGACY_KERAS"] = "1"

# 기존 'import keras' 대신 'tf_keras'를 사용합니다.
from tf_keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# 경로 설정
PATH = os.path.dirname(os.path.abspath(__file__))
print(f"Current Path: {PATH}")

# 과학적 표기법 비활성화
np.set_printoptions(suppress=True)

# 2. 모델 로드 (경로 결합 방식 개선)
model_path = os.path.join(PATH, "keras_model.h5")
labels_path = os.path.join(PATH, "labels.txt")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {model_path}")

model = load_model(model_path, compile=False)

# 3. 라벨 로드
with open(labels_path, "r", encoding="utf-8") as f:
    class_names = [line.strip() for line in f.readlines()]

# 4. 이미지 처리 및 예측
def predict_image(img_name):
    # 경로 구분자(\\) 문제 방지를 위해 os.path.join 사용
    img_path = os.path.join(PATH, "images", img_name)
    
    if not os.path.exists(img_path):
        print(f"이미지 파일을 찾을 수 없습니다: {img_path}")
        return

    image = Image.open(img_path).convert("RGB")

    # 이미지 리사이징 및 중앙 크롭
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # 넘파이 배열 변환 및 정규화
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # 모델 입력용 데이터 생성 (배치 차원 추가)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # 예측 실행
    prediction = model.predict(data)
    index = np.argmax(prediction)
    
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # 결과 출력
    print(f"\n[결과] 파일명: {img_name}")
    # 라벨 파일 형식이 "0 Cat" 형태일 경우 숫자 제거 후 출력
    print(f"Class: {class_name}")
    print(f"Confidence Score: {confidence_score:.4f}")

# 실행
predict_image("dog_5.jpg")