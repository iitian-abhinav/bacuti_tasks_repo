import streamlit as st  #time 30:30

genre=st.selectbox("Select your favorite genre:",
                   ['Comedy','Drama','Documentary','Action','Horror'])
st.write(f"You selected: {genre}"   )

multi_genre=st.multiselect("Select all genres you like:",
                           ['Comedy','Drama','Documentary','Action','Horror'])
st.write(f"You selected: {multi_genre}")

age=st.slider("Select your age:",0,100,1)
st.write('Age',age)

number=st.number_input("Enter a number:",min_value=0,max_value=100,value=1)
st.write('You entered:',number)

bio=st.text_area("Write a short bio:")
st.write("Your bio:",bio)

date=st.date_input("Select a date:",min_value=None,max_value=None,value=None)
st.write("You selected:",date)

time=st.time_input("Select a time:")
st.write("You selected:",time)

upload=st.file_uploader("Upload a file:",type=['png','jpg','jpeg','pdf','txt'])
if upload is not None:
    st.write("File uploaded:",upload.name)
