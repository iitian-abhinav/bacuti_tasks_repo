# ----- Frouping Widgets into forms -----
import streamlit as st 

st.title("forms demo")

with st.form("contact form"):
    name=st.text_input("Name")
    email=st.text_input("Email")
    message=st.text_area("Message")
    submitted=st.form_submit_button("Submit")

if submitted:
    st.write("Thank you for your message, ", name)


st.title("Form Version 2")

with st.form("Calc_form"):

    num1=st.number_input("Number 1")
    num2=st.number_input("Number 2")
    operation=st.selectbox("Operation",["Add","Subtract","Multiply","Divide"])
    calc_submitted=st.form_submit_button("Calculate")

if calc_submitted:
    if operation=="Add":
        result=num1+num2
    elif operation=="Subtract":
        result=num1-num2
    elif operation=="Multiply":
        result=num1*num2
    else:
        result=num1/num2
    st.write("The result is: ", result)

