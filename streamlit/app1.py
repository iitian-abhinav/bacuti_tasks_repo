import streamlit as st

name = st.text_input("Enter your name:", key="name_input")
st.write(f"Hello, {name}!")

if st.button('Click Me!'):
    st.write("Button clicked!")

choice=st.radio("Choose an option:",['ABC','DEF','GHI'])
st.write(f"You selected: {choice}")

agree=st.checkbox('I agree')
if agree:
    st.write("Thank you for agreeing!")