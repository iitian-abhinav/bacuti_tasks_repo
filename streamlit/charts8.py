import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Built-in Charts Example")

# Generate data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.subheader("Line Chart")
st.line_chart(data)

st.subheader("Area Chart")
st.area_chart(data)

st.subheader("Bar Chart")
st.bar_chart(data)

data['c_size'] = data['c'].abs()

st.subheader("Plotly Scatter Chart")
fig = px.scatter(
    data,
    x='a',
    y='b',
    color='c',         # color can be negative
    hover_name='c',
    size_max=60
)

st.plotly_chart(fig)
