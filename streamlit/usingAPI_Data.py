import streamlit as st
import requests
import pandas as pd

st.title("Bitcoin price tracker")

price_url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
history_url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params={"vs_currency":"inr","days":"30","interval":"daily"}

try:
    price_response=requests.get(price_url,timeout=10)
    price_response.raise_for_status()
    price=price_response.json()['bitcoin']['inr']
    st.metric(label="Current Bitcoin Price (INR)",value=f"₹ {price:,}")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching Bitcoin price: {e}")

try:
    history_response=requests.get(history_url,params=params,timeout=10)
    history_response.raise_for_status()
    history_data=history_response.json()['prices']
    df=pd.DataFrame(history_data,columns=['Timestamp','Price'])
    df['Timestamp']=pd.to_datetime(df['Timestamp'],unit='ms')
    df.set_index('Timestamp',inplace=True)
    st.line_chart(df['Price'],height=400,use_container_width=True)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching Bitcoin price history: {e}")

