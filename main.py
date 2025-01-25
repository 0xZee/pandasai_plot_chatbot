#from __future__ import annotations
import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm import BambooLLM
from pandasai.response.response_parser import ResponseParser
from data import get_stock_data

st.set_page_config(page_title="Data Chat Assistant", layout="wide")

st.subheader("# Data Visualization ChatBot", divider='orange')


# Custom response handler for interactive charts
class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)
        #self.query = context.query.lower()

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return


PANDASAI_API_KEY = st.secrets['PANDASAI_API_KEY']
llm = BambooLLM(api_key=PANDASAI_API_KEY)
llm_config = {
    "llm": llm,
    "verbose": True,
    #"conversational": conversational,
    #"enforce_privacy": enforce_privacy,
    #"save_logs": True,
    #"enable_cache": True,
    "max_retries": 3,
    "response_parser": StreamlitResponse,
    }

if st.button("Load Stocks Data", use_container_width=True):
    data = get_stock_data()
    st.info("Data Stocks Loaded")
    with st.expander("**# Stocks Data Overview**"):
        st.dataframe(data.style.highlight_max(axis=0), hide_index=True,)
    st.divider()
    query = st.text_input("Your Query")

    if query:
        df = data
        query_engine = SmartDataframe(
            df,
            name="Stocks financial info",
            description="financial info and data of tech stocks in nasdaq",
            config=llm_config
            )
        answer = query_engine.chat(query)
        st.write(answer)
