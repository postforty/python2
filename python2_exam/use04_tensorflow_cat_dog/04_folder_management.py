import os
import shutil

# 1. 원본 폴더와 결과 폴더 경로 설정
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "images")
result_path = os.path.join(base_path, "result")

# 2. 결과 폴더가 존재하지 않는 경우 자동으로 생성
if not os.path.exists(result_path):
    os.makedirs(result_path)
    print(f"새 폴더 생성 완료: {result_path}")

# 3. 폴더 내 파일들을 결과 폴더로 복사하기
if os.path.exists(image_path):
    files = os.listdir(image_path)
    for file_name in files:
        src = os.path.join(image_path, file_name)
        dst = os.path.join(result_path, file_name)
        
        # shutil.copy2는 원본 파일의 정보를 유지하며 복사합니다.
        shutil.copy2(src, dst)
        print(f"파일 복사 완료: {file_name} -> result 폴더")
else:
    print(f"복사할 원본 폴더가 없습니다: {image_path}")

print("\n--- 모든 작업을 마쳤습니다. ---")
