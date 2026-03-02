import streamlit as st

st.title("Multi tab App")
tabs=st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tabs[0]:
    st.write("This is the first tab")
with tabs[1]:
    st.write("This is the second tab")
with tabs[2]:
    st.write("This is the third tab")