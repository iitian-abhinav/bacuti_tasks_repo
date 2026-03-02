import streamlit as st

password_input = st.text_input("Enter the password to access this content:", type="password")

if password_input == st.secrets['auth']['password']:
    st.write("Access granted! Here is the protected content.")
    # Place your protected content code here
else:
    st.write("Access denied! Please enter the correct password.")

if 'user role' not in st.session_state:
    st.session_state.user_role=None

def login(user):
    role={'admin':'admin','user':'viewer'}
    st.session_state.user_role=role.get(user,'viewer')

user=st.text_input("User name")

if st.button("Login"):
    login(user)

if st.session_state.user_role=='admin':
    st.success("Welcome admin you have full access.")
    st.write('Admin content')

elif st.session_state.user_role=='viewer':
    st.success("Welcome viewer you have limited access.")
    st.write('Viewer content')
else:
    st.warning("Please login to access the content.")