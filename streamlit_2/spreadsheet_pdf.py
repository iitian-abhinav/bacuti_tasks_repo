import streamlit as st
import pandas as pd
from io import BytesIO
import base64
from fpdf import FPDF

st.title("Export data demo")

df=pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'races': ['100m', '200m', '400m']
})

st.dataframe(df)

# CSV download
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv'
    )

#excel download
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

excel_data = to_excel(df)
st.download_button(
    label="Download data as Excel",
    data=excel_data,
    file_name='data.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)
