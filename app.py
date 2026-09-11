import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image


# Page settings
st.set_page_config(
    page_title="Bird Species Classification",
    page_icon="🐦"
)


# Paths
MODEL_PATH = "models/bird_species_model.keras"
CLASS_NAMES_PATH = "models/class_names.json"


# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


# Load class names
@st.cache_data
def load_class_names():
    with open(CLASS_NAMES_PATH, "r") as file:
        return json.load(file)


model = load_model()
class_names = load_class_names()


# Title
st.title("🐦 Bird Species Classification")

st.write(
    "Upload a bird image to predict its species."
)


# Upload image
uploaded_file = st.file_uploader(
    "Upload a Bird Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Display uploaded image
    st.image(
        image,
        caption="Uploaded Bird Image"
    )

    # Get model input size
    img_height = model.input_shape[1]
    img_width = model.input_shape[2]

    # Resize image
    image = image.resize(
        (img_width, img_height)
    )

    # Convert to numpy
    image_array = np.array(image)

    # Normalize
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Prediction
    predictions = model.predict(
        image_array,
        verbose=0
    )

    # Get predicted class
    predicted_index = np.argmax(predictions[0])

    predicted_species = class_names[predicted_index]

    # Confidence
    confidence = predictions[0][predicted_index] * 100


    # Display result
    st.success(
        f"Predicted Species: {predicted_species}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )