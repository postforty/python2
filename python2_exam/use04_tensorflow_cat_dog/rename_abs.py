import os

base_dir = r"c:\Users\dandycode\Documents\GitHub\python2\python2_exam\use04_tensorflow_cat_dog"

mapping = {
    "01_keras_modal_test.py": "01_keras_model_test.py",
    "02_파일_목록_출력.py": "02_file_listing.py",
    "03_넘파이_정규화_실습.py": "03_numpy_normalization.py",
    "04_폴더_생성_및_복사.py": "04_folder_management.py",
    "cat_dog_taster.py": "cat_dog_classifier.py"
}

for old, new in mapping.items():
    old_full = os.path.join(base_dir, old)
    new_full = os.path.join(base_dir, new)
    if os.path.exists(old_full):
        try:
            os.rename(old_full, new_full)
            print(f"SUCC: {old} -> {new}")
        except Exception as e:
            # Try to read the directory to check for encoding mismatches
            print(f"FAIL: {old} -> {new} ({e})")
    else:
        print(f"NOTFOUND: {old}")

print(f"Actual files on disk: {os.listdir(base_dir)}")
