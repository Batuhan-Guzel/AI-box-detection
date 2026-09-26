from ultralytics import YOLO
import streamlit as st
from PIL import Image

model = YOLO("runs/detect/train-3/weights/best.pt")

st.title("Damaged Box Detection")

uploaded = st.file_uploader("Upload a box image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded)

    results = model(image)

    plotted = results[0].plot()

    st.image(plotted, caption="Detection Result")