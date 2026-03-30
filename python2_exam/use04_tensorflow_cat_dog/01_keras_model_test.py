# Teachable Machine: https://teachablemachine.withgoogle.com/
# 2024-04-28 tensorflow version: https://pypi.org/project/tensorflow/2.15.1/
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os

# Get path
PATH = os.path.dirname(__file__)
print(f"Current Path: {PATH}")

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(os.path.join(PATH, "keras_model.h5"), compile=False)

# Load the labels
with open(os.path.join(PATH, "labels.txt"), "r") as f:
    class_names = f.readlines()

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Load the image
image = Image.open(os.path.join(PATH, "cat_182.jpg")).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)
