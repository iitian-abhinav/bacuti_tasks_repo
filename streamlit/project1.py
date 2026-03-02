import streamlit as st
import pandas as pd

st.sidebar.title('Navigation    ')

section=st.sidebar.radio("Go to",["About","Skills","Experience","Education","Contact"])

skils={
    'Python':0.8,
    'Machine Learning':0.7,
    'Streamlit':0.8,
    'SQL':0.75,
    'Data Analysis':0.85,
    'Data Visualization':0.87
}

st.title('Abhinav ')
st.subheader('Data Analyst')

if section=="About":
    st.header('About Me')
    st.write("""
    I am a passionate Data Analyst with expertise in Python, Machine Learning, and Data Visualization. 
    I love turning data into actionable insights and helping businesses make informed decisions.
    """)
elif section=="Skills":
    st.header('Skills')
    for skill, proficiency in skils.items():
        st.write(f"{skill}")
        st.progress(proficiency)
    df_skills=pd.DataFrame({
        'Skills':list(skils.keys()),
        'proficiency':list(skils.values())
    })
    st.bar_chart(df_skills.set_index('Skills'))

elif section=="Experience":
    st.header('Work Experience')
    with st.expander("Junior Data Analyst at ABC Inc (2018 - 2020)"):
        st.write("""
        - Assisted in data cleaning and preprocessing tasks.
        - Created visualizations to support business decisions.
        - Conducted statistical analysis to identify trends and patterns.
        """) 
    with st.expander("Data Analyst at XYZ Corp (2020 - Present)"):
        st.write("""
        - Analyzed large datasets to extract actionable insights.
        - Developed dashboards and reports using Streamlit and Tableau.
        - Collaborated with cross-functional teams to implement data-driven strategies.
        """)
    

elif section=="Education":
    st.header('Education')
    with st.expander("B.Sc. in Computer Science, University of Somewhere (2014 - 2018)"):
        st.write("""
        - Relevant Coursework: Data Structures, Algorithms, Database Management, Statistics.
        - Graduated with Honors.
        """)
    with st.expander("Certified Data Analyst, DataCamp (2019)"):
        st.write("""
        - Completed courses on Python for Data Analysis, Machine Learning, and Data Visualization.
        """)
    

elif section=="Contact":
    st.header("Get in Touch")
    col1, col2 = st.columns(2)
    with col1:
        email=st.text_input("Email Address")
        phone=st.text_input("Phone Number")
    with col2:
        linkedin=st.text_input("LinkedIn Profile URL")
        message=st.text_area("Your Message")
    if st.button("Submit"):
        st.success("Thank you for reaching out! I will get back to you soon.")
    
    