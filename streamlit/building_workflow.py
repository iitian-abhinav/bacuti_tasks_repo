import streamlit as st
st.title("Step by step workflow")

if "step" not in st.session_state:
    st.session_state.step=1
if 'name' not in st.session_state:
    st.session_state.name=""
if 'choice'not in st.session_state:
    st.session_state.choice=""

def next_step():
    st.session_state.step+=1

def restart():
    st.session_state.step=1
    st.session_state.name=""
    st.session_state.choice=""

if st.session_state.step == 1:
    st.write("Step 1: Enter your name")
    st.text_input("Name:",value=st.session_state.name,key="name")
    st.button("Next",on_click=next_step)
elif st.session_state.step==2:
    st.write(f"Hello {st.session_state.name}, Step 2: Make a choice")
    st.radio("Choose one:",["Option 1","Option 2","Option 3"],key="choice",index=["Option 1","Option 2","Option 3"].index(st.session_state.choice) if st.session_state.choice in ["Option 1","Option 2","Option 3"] else 0)
    st.button("Next",on_click=next_step)
elif st.session_state.step==3:
    st.write(f"Thank you {st.session_state.name}, you chose {st.session_state.choice}.")
    st.button("Restart",on_click=restart)
