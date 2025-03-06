import os
import streamlit as st

def show():
    st.title("Welcome to Financial Empowerment for Women")

    image_path = "/Users/sanjanadonthula/Documents/iacclerate-1/icon.webp"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)

    else:
        st.warning("Image not found. Please check the file path.")
