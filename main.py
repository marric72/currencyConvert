import streamlit as st
import pandas as pd
import numpy as np

#Write text to the screen
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
#st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 Streamlit Test</p>'
st.markdown(title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
n=st.text_input("Enter name")
if len(n) > 0:
	title = f'<p style="font-family:Courier; color:Blue; font-size: 20px;">Welcome {n}</p>'
	st.markdown(title, unsafe_allow_html=True)

