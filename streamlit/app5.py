import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

img=Image.new('RGB',(200,100),color = 'skyblue')

st.image(img, caption='Sample Image', use_container_width=True)

data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(data)

audio_file = open('sample_audio.mp3', 'rb') if False else None
video_file = open('sample_video.mp4', 'rb') if False else None

if audio_file:
    st.audio(audio_file.read(), format='audio/mp3')
if video_file:
    st.video(video_file.read(), format='video/mp4')

st.video("https://www.youtube.com/watch?v=bPzClIyHUQY")

html_code="""
<div style="background-color: lightblue; padding: 10px;">
    <h2>Sample HTML Content</h2>
    <p>This is a sample paragraph inside an HTML div.</p>
</div>
"""
st.markdown(html_code, unsafe_allow_html=True)