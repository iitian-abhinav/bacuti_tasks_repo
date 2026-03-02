import streamlit as st
import pandas as pd
import json

st.title("File upload and preview ")

uploaded_file=st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx","json"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("CSV Preview:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        st.write("Excel Preview:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith('.json'):
        data = json.load(uploaded_file)
        st.write("JSON Preview:")
        st.json(data)
    else:
        st.error("Unsupported file type. Please upload a CSV, Excel, or JSON file.")

if uploaded_file:
    file_size=uploaded_file.size/1024
    st.write(f"File size: {file_size:.2f} KB")
    if file_size>1024:
        st.warning("The file size exceeds 1 MB, which may affect performance.")

@st.cache_data
def load_large_csv(file):
    return pd.read_csv(file)

st.write("Upload a large CSV file to see caching in action. ")

large_file=st.file_uploader("Upload a large CSV file", type=["csv"], key="large_file")
if large_file:
    df_large = load_large_csv(large_file)
    st.write("Large CSV Preview:")
    st.dataframe(df_large.head())
