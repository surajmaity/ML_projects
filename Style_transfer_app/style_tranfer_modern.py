# Import necessary libraries
import altair as alt
import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

# Set page config FIRST
st.set_page_config(layout="wide")

# Load TensorFlow Hub model
MODEL_URL = "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
hub_model = hub.load(MODEL_URL)

def crop_image(img):
    current_shape = tf.shape(img).numpy()
    new_shape = min(current_shape[0], current_shape[1])
    offset_y = (current_shape[0] - new_shape) // 2
    offset_x = (current_shape[1] - new_shape) // 2
    img = tf.image.crop_to_bounding_box(img, offset_y, offset_x, new_shape, new_shape)
    return img

def load_image(uploaded_file, image_size=(256, 256), col=st):
    img = Image.open(uploaded_file)
    img = tf.convert_to_tensor(img)
    img = crop_image(img)
    img = tf.image.resize(img, image_size)
    if img.shape[-1] == 4:
        img = img[:, :, :3]
    img = tf.expand_dims(img, axis=0) / 255.0
    col.image(np.array(img[0]), use_column_width=True)
    return img

def show_images(images, titles=('',), col=st):
    n = len(images)
    for i in range(n):
        col.image(np.array(images[i][0]), use_column_width=True)

# Custom CSS for modern look
st.markdown(
    """
    <style>
    /* Change font */
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
    }
    
    /* Center align headers */
    h1, h2, h3 {
        text-align: center;
        color: #4CAF50;
    }
    
    /* Add padding and rounded corners to containers */
    .stButton>button {
        border-radius: 20px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    
    /* Add a gradient background */
    .stApp {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white;
    }
    
    /* Style file uploader */
    .stFileUploader>div>div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Add animation to headers */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .fade-in {
        animation: fadeIn 2s;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hide Streamlit default menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main app
if __name__ == "__main__":
    img_width, img_height = 384, 384
    img_width_style, img_height_style = 384, 384
    
    # App title with animation
    st.markdown(
        """
        <div class="fade-in">
            <h1>🎨 Image Style Transfer App</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("Upload your images and let the magic happen! ✨")

    # Columns for image upload
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('### Add Image on Which Style is Required')
        uploaded_file = st.file_uploader("Choose image to change", type=["jpg", "png", "jpeg"], key="content")
        content_image = None
        if uploaded_file is not None:
            content_image = load_image(uploaded_file, (img_width, img_height), col=col1)
    
    with col2:
        st.markdown('### Add Image from Which Style Will Be Extracted')
        uploaded_file_style = st.file_uploader("Choose style image", type=["jpg", "png", "jpeg"], key="style")
        style_image = None
        if uploaded_file_style is not None:
            style_image = load_image(uploaded_file_style, (img_width_style, img_height_style), col=col2)
            style_image = tf.nn.avg_pool(style_image, ksize=[3, 3], strides=[1, 1], padding='SAME')
    
    # Display stylized image
    if content_image is not None and style_image is not None:
        with st.spinner("Applying style... Please wait ✨"):
            outputs = hub_model(tf.constant(content_image), tf.constant(style_image))
            stylized_image = outputs[0]
            st.success("Style applied successfully!")
            st.balloons()
            
            # Display stylized image in the center
            col3, col4, col5 = st.columns([1, 2, 1])
            with col4:
                st.markdown('### 🖼️ Style Applied on the Image')
                show_images([stylized_image], titles=['Stylized image'], col=col4)

    # Footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #2E3440;
            color: white;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>Made by suraj with ❤️ using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )