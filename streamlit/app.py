import streamlit as st
# NOTE: to run this file use: python -mm streamlit run filename.py

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.markdown("**MARKDOWN** _is_ supported! [visit stramlit](https://streamlit.io)")

st.text("This is a plain text")

st.markdown("### Code Block Example")
st.code("""
# Python example
def greet(name):
    return f"Hello, {name}!
print(greet(input("Enter your name: ")))
        """, language='python')

st.success("This is a success message!")
st.warning("This is a warning message!")
st.error("This is an error message!")
st.info("This is an informational message.")
st.markdown("> This is a blockquote example.")