import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data
def get_stock_data():
    # Example usage
    tickers = ['AAPL', 'NVDA', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'AVGO', 'WMT', 'LLY', 'ORCL', 'COST', 'NFLX', 'NVO', 'CRM', 'KO', 'CSCO', 'NOW', 'IBM', 'BABA', 'GE', 'AMD', 'DIS', 'ADBE', 'QCOM', 'PLTR', 'RTX', 'ARM', 'ANET', 'NEE', 'HON', 'UBER', 'SHOP', 'MU', 'PANW', 'APP', 'MRVL', 'BYDDY', 'NKE', 'CEG', 'SPOT', 'MSTR', 'PYPL', 'INTC', 'CRWD', 'COIN', 'FTNT', 'WDAY', 'JD', 'TTD', 'VST', 'SNOW', 'SQ', 'DDOG', 'HOOD', 'NET', 'RDDT', 'ZS', 'IOT', 'TER', 'PSTG', 'ALAB', 'MDB', 'GRAB', 'SMCI', 'AFRM', 'SOFI', 'NTNX', 'CYBR', 'OKTA', 'RIVN', 'XPEV', 'RBRK', 'MNDY', 'AUR', 'ROKU', 'RKLB', 'ONTO', 'GTLB', 'PSN', 'EXAS', 'LCID', 'NIO', 'ENPH', 'IONQ', 'AES', 'PATH', 'S', 'ASTS', 'LYFT', 'TEM', 'BE', 'SOUN', 'KTOS', 'AVAV', 'PONY', 'BEPC', 'BRZE', 'ACHR', 'AI', 'VKTX', 'OKLO', 'GSAT', 'CRSP', 'RGTI', 'SMR', 'QS', 'RXRX', 'RPD', 'KC', 'PLUG', 'APLD', 'BEAM', 'TXG', 'LUNR', 'TDOC', 'QBTS', 'SDGR', 'FSLY', 'OLO', 'DQ', 'QUBT', 'PL', 'TLRY', 'BBAI', 'RDW', 'SERV', 'NTLA', 'NNE', 'RCAT', 'DNA', 'RZLV', 'KULR', 'NNOX', 'CHPT', 'PACB', 'SPIR', 'LAES', 'QSI', 'VLN', 'RR', 'BKSY', 'ARQQ', 'CGC', 'ARBE', 'ACB', 'NUKK', 'QMCO', 'REKR', 'OPTT', 'NKLA', 'EDIT', 'INTZ', 'MDAI', 'SIDU', 'EKSO']
    list_keys = ['symbol', 'shortName', 'country','industry','sector','currentPrice','marketCap', 'trailingPE', 'forwardPE', 'priceToSalesTrailing12Months', 'priceToBook', 'debtToEquity','shortRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 'beta', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'targetMeanPrice', 'targetHighPrice', 'recommendationKey','returnOnEquity', 'totalRevenue', 'freeCashflow', 'totalDebt', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins','trailingPegRatio']
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        # Create a dictionary with keys from list_keys, using None for missing values
        row = {key: info.get(key) for key in list_keys}
        data.append(row)
    return pd.DataFrame(data)
