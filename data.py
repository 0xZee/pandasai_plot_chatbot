import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data
def get_stock_data():
    # Example usage
    tickers = ["AAPL","GOOGL", "MSFT","ORCL", "NOW","SNOW", "PLTR","IONQ", "NVDA", "ASTS", "RKLB", "QBTS", "RXRX", "AMD", "LAES", "GSAT", "LUNR"]
    list_keys = ['symbol', 'currentPrice','marketCap', 'trailingPE', 'forwardPE', 
                'priceToSalesTrailing12Months', 'shortRatio', 'enterpriseToRevenue', 
                'enterpriseToEbitda', 'targetHighPrice', 'returnOnEquity']
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        # Create a dictionary with keys from list_keys, using None for missing values
        row = {key: info.get(key) for key in list_keys}
        data.append(row)
    return pd.DataFrame(data)
