import streamlit as st # video: 39:48
import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data)

st.markdown("### User Information")
st.write(df)
st.markdown("### Static Table")
st.table(df)
st.markdown("### DataFrame with Interactive Features")
st.dataframe(df)

person={
    'Name': 'Eve',
    'Age': 28,
    'City': 'San Francisco'
}

st.json(person)
st.write("dictionary displayed with st.json")

editable_df=st.data_editor(df,num_rows='dynamic')
st.markdown("### Editable DataFrame")
st.write(editable_df)