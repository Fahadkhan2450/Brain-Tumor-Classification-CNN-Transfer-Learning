import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "vgg16_brain_tumor (1).keras"

model = tf.keras.models.load_model(MODEL_PATH)

class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

IMAGE_PATH = "/Users/malikfahad/Desktop/Machine learning/Brain Mri/Backend/No tumor.jpg"   # put one known test image here

image = Image.open(IMAGE_PATH).convert("RGB")

image = image.resize(
    (128, 128),
    Image.Resampling.LANCZOS
)

image = np.array(
    image,
    dtype=np.float32
)

image = image / 255.0

image = np.expand_dims(
    image,
    axis=0
)

pred = model.predict(
    image,
    verbose=0
)[0]

print("\nPrediction probabilities:")

for name, probability in zip(class_names, pred):
    print(
        f"{name:15s}: {probability * 100:.2f}%"
    )

index = np.argmax(pred)

print("\nPredicted:", class_names[index])
print("Confidence:", f"{pred[index] * 100:.2f}%")