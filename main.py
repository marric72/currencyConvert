import streamlit as st
import pandas as pd
import numpy as np
from requests import get


st.set_page_config(
    page_title="Capture The Flag",
    page_icon="🚩",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">prclab1 Capture the Flag</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)


instructions='<p style="font-family:Courier; color:Blue; font-size: 20px;">Start on <b>prclab1</b> in the directory <b>/home/faculty/marric72/cs125_CTF</b> <br>Use the commands we learned in class (ex. cd, cat, ls) to navigate and find the flags.  Enter your answers in the boxes to the right of the questions and then hit Check Answers.<br>Happy Hunting! (Hint: Flags look like: FLG-####)<br><br>Sometimes I do not want to give the whole file name, so I use stars in place of characters below.</p>'
st.markdown(instructions, unsafe_allow_html=True)
st.markdown(instructions, unsafe_allow_html=True)

#st.write("Pulling data from: https://api.exchangerate-api.com/v4/latest/USD")
#url = 'https://api.exchangerate-api.com/v4/latest/USD'
#result=get(url, timeout=3).json()

# Convert rates data to DataFrame
#df = pd.DataFrame(result.get("rates"), index=["Rates"])

# Display multi-select for choosing columns
#selected_columns = st.multiselect(
#    'Select columns to display:',
#    list(df.columns),
#    default=['USD', 'EUR', 'GBP']  # Default columns to display
#)

# Filter DataFrame based on selected columns
#filtered_df = df[selected_columns]

# Display the filtered DataFrame
#st.title("All the Data")
#st.write(filtered_df)

