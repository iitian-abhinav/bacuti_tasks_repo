import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.title("3rd party components")

def load_lottie_url(url):
    r=requests.get(url)
    if r.status_code==200:
        return r.json()
    else:
        return None
    
lottie_url="https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_json=load_lottie_url(lottie_url)
if lottie_json:
    st_lottie(lottie_json, speed=1, width=300, height=300, key="animation")