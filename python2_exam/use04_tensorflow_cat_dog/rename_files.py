import os
import glob

files = glob.glob("*.py")
print(f"Found files: {files}")

mapping = {
    "02_": "02_file_listing.py",
    "03_": "03_numpy_normalization.py",
    "04_": "04_folder_management.py",
    "cat_dog_taster": "cat_dog_classifier.py",
    "01_": "01_keras_model_test.py"
}

for f in files:
    for prefix, new_name in mapping.items():
        if f.startswith(prefix):
            try:
                os.rename(f, new_name)
                print(f"Renamed: {f} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {f} to {new_name}: {e}")
            break
