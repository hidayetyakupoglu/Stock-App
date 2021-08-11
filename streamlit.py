import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# This takes input from the user on which stock ticker that they would like to look at and gives a sliding scale to choose how much data to look back at in months
tickerSymbol = st.text_input("Enter a ticker symbol: ", "GME")
monthsSlider = st.slider("Number of Previous Months", min_value=1, max_value = 60, value = 12, step = 1)

tickerData = yf.Ticker(tickerSymbol)

companyName = tickerData.info['longName']

#
endDay = date.today()
startDay = endDay - relativedelta(months=monthsSlider)

tickerDf = tickerData.history(period = '1d', start=startDay, end=endDay)

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of %s!

""" % companyName)

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)