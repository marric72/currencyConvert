import streamlit as st
import pandas as pd
import numpy as np

#Write text to the screen
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
#st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 Streamlit Test</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("money.png", caption='Save your Money')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
n=st.text_input("Enter name")
if len(n) > 0:
	title = f'<p style="font-family:Courier; color:Blue; font-size: 20px;">Welcome {n}</p>'
	st.markdown(title, unsafe_allow_html=True)

from requests import get

options = st.multiselect(
    'What are your biggest expenses?',
    ['Food', 'Rent', 'Car', 'Clothes', 'Electronics', 'Other'],
    default=['Food', 'Rent'])

st.markdown(options, unsafe_allow_html=True)

#st.write('You selected favorite colors:<span style="color:black;">', options, "</span>")

#st.write('You selected favorite colors:', options)

st.write("  ")
st.write(" -------------------------------------------- ")

st.write("Pulling data from: https://api.exchangerate-api.com/v4/latest/USD")
url = 'https://api.exchangerate-api.com/v4/latest/USD'
result=get(url, timeout=3).json()

# Convert rates data to DataFrame
df = pd.DataFrame(result.get("rates"), index=["Rates"])

# Display multi-select for choosing columns
selected_columns = st.multiselect(
    'Select columns to display:',
    list(df.columns),
    default=['USD', 'EUR', 'GBP']  # Default columns to display
)

# Filter DataFrame based on selected columns
filtered_df = df[selected_columns]

# Display the filtered DataFrame
st.title("All the Data")
st.write(filtered_df)


#print(result['date'])
#print(result['rates'])
st.title("Exchange Rate")
st.table(result.get("rates"))


