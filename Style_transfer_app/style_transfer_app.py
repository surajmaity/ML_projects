# Import necessary libraries
import altair as alt
import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

MODEL_URL = "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
hub_model = hub.load(MODEL_URL)
#crop the image to the model's input size ,whatever the aspect ratio it converts it to a square
def crop_image(img):
    current_shape = tf.shape(img).numpy()
    new_shape = min(current_shape[0], current_shape[1])
    offset_y = (current_shape[0] - new_shape) // 2
    offset_x = (current_shape[1] - new_shape) // 2
    img = tf.image.crop_to_bounding_box(img, offset_y, offset_x, new_shape, new_shape)
    return img
#image loading and processing
def load_image(uploaded_file, image_size=(256, 256), col=st):
    img = Image.open(uploaded_file)
    img = tf.convert_to_tensor(img)
    img = crop_image(img)
    img = tf.image.resize(img, image_size)
    #if the image has an alpha channel, remove it as the model only works with RGB images
    if img.shape[-1] == 4:
        img = img[:, :, :3]
    #resize the image to the model's input size and normalize the pixel values to be between 0 and 1
    img = tf.expand_dims(img, axis=0) / 255.0
    col.image(np.array(img[0]))
    return img

def show_images(images, titles=('',), col=st):
    n = len(images)
    for i in range(n):
        col.image(np.array(images[i][0]))

st.set_page_config(layout="wide")
alt.renderers.set_embed_options(scaleFactor=2)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    img_width, img_height = 384, 384
    img_width_style, img_height_style = 384, 384
    col1, col2 = st.columns(2)
    
    col1.markdown('# Add image on which style is required')
    uploaded_file = col1.file_uploader("Choose image to change")
    content_image = None
    if uploaded_file is not None:
        content_image = load_image(uploaded_file, (img_width, img_height), col=col1)
    
    col2.markdown('# Add image from which style will be extracted')
    uploaded_file_style = col2.file_uploader("Choose style image")
    style_image = None
    if uploaded_file_style is not None:
        style_image = load_image(uploaded_file_style, (img_width_style, img_height_style), col=col2)
        style_image = tf.nn.avg_pool(style_image, ksize=[3, 3], strides=[1, 1], padding='SAME')
    
    if content_image is not None and style_image is not None:
        outputs = hub_model(tf.constant(content_image), tf.constant(style_image))
        stylized_image = outputs[0]
        col3, col4, col5 = st.columns(3)
        col4.markdown('# Style applied on the image')
        show_images([stylized_image], titles=['Stylized image'], col=col4)