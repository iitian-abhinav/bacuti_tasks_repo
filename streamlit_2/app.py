import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Stock Price App",
    page_icon='📈',
    layout='wide')
st.title("Stock Price App")

st.sidebar.header("Stock Settings")

ticker_symbol = st.sidebar.text_input("Enter Stock Ticker", value="AAPL", max_chars=5)
period=st.sidebar.selectbox("Select Period", options=["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"], index=5)
interval=st.sidebar.selectbox("Select Interval", options=["1m", "2m", "5m", "15m", "30m", "60m", "90m",
                                                          
                                                            "1h", "1d", "5d", "1wk", "1mo", "3mo"], index=8)

ticker=yf.Ticker(ticker_symbol)
data=ticker.history(period=period, interval=interval)

latest_price=data['Close'][-1] if not data.empty else 'N/A'
st.metric(label=f"Latest Closing Price of {ticker_symbol}", value=f"${latest_price:.2f}" if latest_price != 'N/A' else latest_price)

st.subheader(f"Historical Data for {ticker_symbol}")
if not data.empty:
    st.line_chart(data['Close'])
    st.dataframe(data)
else:
    st.write("No data available for the given ticker symbol and parameters.")

col1,col2,col3=st.columns(3)

with col1: 
    st.write("Previous Closed",ticker.info.get('previousClose','N/A'))
with col2:
    st.write("Market Cap",ticker.info.get('marketCap','N/A'))
with col3:
    st.write("52 week high",ticker.info.get('fiftyTwoWeekHigh','N/A'))

st.caption("Refresh page for updated data.")