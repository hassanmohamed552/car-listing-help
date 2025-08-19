import streamlit as st
from json_parser import chain
from dummy_cv import classify_car_type
from email_utils import send_email
import tempfile
import os

st.title("🚗 Car Listing Helper")

description = st.text_area("Enter car description")
image = st.file_uploader("Upload car image", type=["jpg", "jpeg", "png"])

if st.button("Submit"):
    if not description or not image:
        st.error("Please provide both description and image.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(image.read())
            image_path = tmp.name

        result = chain.invoke({"car_description": description})
        result.car.body_type = classify_car_type(image_path)

        send_email(result.dict(), image_path, "hassan.elzoheery@live.com")
        st.success("✅ Email sent successfully!")

        os.remove(image_path)
