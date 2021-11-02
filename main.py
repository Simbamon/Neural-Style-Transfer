import streamlit as st
from PIL import Image

import style

st.set_page_config(layout="wide")
st.title("Cloud Pak for Data X PyTorch")

img = st.sidebar.selectbox(
    '이미지를 선택하세요',
    ('amber.jpg', 'profile.jpg', 'poster.jpg', 'city.jpg', 'nature.jpg')
)

style_name = st.sidebar.selectbox(
    '스타일을 선택하세요',
    ('candy', 'mosaic', 'rain-princess', 'udnie')
)

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
style_image = "images/style-images/" + style_name + ".jpg"
output_image = "images/output-images" + img

col1, col2, col3 = st.columns(3)

image = Image.open(input_image)
col1.write("### 기본 이미지:")
col1.image(image, width=420)

col2.write("### 스타일 이미지:")
image2 = Image.open(style_image)
col2.image(image2, width=420)

clicked = st.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    col3.write("### 결과:")
    image = Image.open(output_image)
    col3.image(image, width=420)


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 