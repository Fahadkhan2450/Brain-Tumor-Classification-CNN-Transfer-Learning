import io
import numpy as np
import tensorflow as tf

from PIL import Image

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware


# ==========================================
# FASTAPI
# ==========================================

app = FastAPI(
    title="Brain MRI Tumor Classification API",
    version="1.0.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ==========================================
# LOAD VGG16 MODEL
# ==========================================

MODEL_PATH = "vgg16_brain_tumor (1).keras"

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)


# ==========================================
# CLASS NAMES
# IMPORTANT:
# Must match training label order
# ==========================================

class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

IMG_SIZE = (128, 128)


# ==========================================
# PREPROCESS IMAGE
# EXACTLY MATCHES TRAINING
# ==========================================

def preprocess_image(image):

    # RGB
    image = image.convert("RGB")

    # Resize exactly like training
    image = image.resize(
        IMG_SIZE,
        Image.Resampling.LANCZOS
    )

    # Convert to NumPy float32
    image = np.array(
        image,
        dtype=np.float32
    )

    # IMPORTANT:
    # DO NOT divide by 255.
    #
    # Your working training pipeline uses:
    #
    # image = image.astype(np.float32)
    #
    # Therefore API must use the same scale.

    # Add batch dimension
    image = np.expand_dims(
        image,
        axis=0
    )

    return image


# ==========================================
# PREDICTION
# ==========================================

def predict_image(image):

    # Preprocess
    processed_image = preprocess_image(
        image
    )

    # Model prediction
    predictions = model.predict(
        processed_image,
        verbose=0
    )[0]

    # Predicted class
    index = int(
        np.argmax(predictions)
    )

    predicted_class = class_names[index]

    confidence = float(
        predictions[index] * 100
    )

    # All class probabilities
    probabilities = {
        class_names[i]: round(
            float(predictions[i] * 100),
            2
        )
        for i in range(
            len(class_names)
        )
    }

    return (
        predicted_class,
        confidence,
        probabilities
    )


# ==========================================
# PREDICT API
# ==========================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    try:

        # Check file type
        if not file.content_type.startswith(
            "image/"
        ):
            return {
                "error": "Please upload a valid image file."
            }

        # Read uploaded image
        contents = await file.read()

        # Open image
        image = Image.open(
            io.BytesIO(contents)
        )

        # Prediction
        (
            predicted_class,
            confidence,
            probabilities
        ) = predict_image(image)

        return {

            "success": True,

            "prediction":
                predicted_class,

            "confidence":
                round(
                    confidence,
                    2
                ),

            "probabilities":
                probabilities

        }

    except Exception as e:

        return {

            "success": False,

            "error":
                str(e)

        }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/")
def home():

    return {

        "status":
            "online",

        "model":
            "VGG16",

        "input_size":
            "128x128",

        "classes":
            class_names

    }
