# -*- coding:UTF-8 -*-
import streamlit as st
from PIL import Image
def run_home():
    st.markdown("# MARMOT")
    img = Image.open('datas/image_1.jpg')
    st.image(img)

width, height = img.size
smaill = img.resize((width//2,height//2), Image.ANTIALIAS)
smaill.save('datas/image_1.jpg', 'jpg')