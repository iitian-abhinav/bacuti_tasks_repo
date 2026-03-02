import streamlit as st

pages=["Home","Dashboard","Settings"]
choice = st.sidebar.radio("Select a page:",pages)

if choice=="Home":
    st.header("Home Page")
    st.write("Welcome to the Home Page!")
elif choice=="Dashboard":
    st.header("Dashboard")
    st.write("This is the Dashboard where you can see your data.")
elif choice=="Settings":
    st.header("Settings")
    st.write("Adjust your preferences here.")