import streamlit as st
import pandas as pd
import numpy as np
from requests import get


#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 Streamlit Test</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("money.png", caption='Save your Money')

options = st.multiselect(
    'What are your biggest expenses?',
    ['Food', 'Rent', 'Car', 'Clothes', 'Electronics', 'Other'],
    default=['Food', 'Rent'])

st.write("Your main expenses are:")
st.markdown(options, unsafe_allow_html=True)

