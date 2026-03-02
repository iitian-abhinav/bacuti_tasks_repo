import streamlit as st
import pandas as pd
import numpy as np

data=pd.DataFrame({
    'Category': ['A','A','B','B','C','C'],
    'subcategory': ['X','Y','X','Y','X','Y'],
    'value':np.random.randint(10,100,6)
})

category=st.selectbox('Select Category', data['Category'].unique())

filtered_data=data[data['Category']==category]

st.write(f"Data for Category {category}:")
st.table(filtered_data)
