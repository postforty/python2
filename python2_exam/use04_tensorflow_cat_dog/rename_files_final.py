import os

files = os.listdir(".")
print(f"Directory files: {files}")

mapping = {
    "02": "02_file_listing.py",
    "03": "03_numpy_normalization.py",
    "04": "04_folder_management.py",
    "cat_dog_taster": "cat_dog_classifier.py",
    "01_keras_modal": "01_keras_model_test.py"
}

for f in files:
    for key, new_name in mapping.items():
        if f.startswith(key):
            try:
                os.rename(f, new_name)
                print(f"RENAME SUCCESS: {f} -> {new_name}")
            except Exception as e:
                print(f"RENAME FAILED: {f} -> {new_name} ({e})")
