import os
import glob

# 1. 현재 파일이 위치한 폴더 경로 가져오기
base_path = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(base_path, "images") # 실습용 images 폴더

print(f"조회할 폴더: {target_path}")

# 2. 폴더 내의 모든 파일 목록 가져오기 (os.listdir 사용)
print("\n--- 모든 파일 목록 ---")
if os.path.exists(target_path):
    files = os.listdir(target_path)
    for f in files:
        print(f"파일명: {f}")
else:
    print("폴더가 존재하지 않습니다.")

# 3. 특정 확장자(*.jpg)만 골라내기 (glob 사용)
print("\n--- 이미지 파일(*.jpg)만 골라내기 ---")
image_files = glob.glob(os.path.join(target_path, "*.jpg"))
for img in image_files:
    # os.path.basename은 경로에서 파일 이름만 추출합니다.
    print(f"이미지 경로: {img}")
    print(f"이미지 이름: {os.path.basename(img)}")
