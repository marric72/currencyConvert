import streamlit as st
import pandas as pd
import numpy as np
from requests import get


#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 Streamlit Test</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("money.png", caption='Save your Money')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)

st.write("Pulling data from: https://api.exchangerate-api.com/v4/latest/USD")
url = 'https://api.exchangerate-api.com/v4/latest/USD'
result=get(url, timeout=3).json()

st.title("All the Data")
st.table(result.get("rates"))


