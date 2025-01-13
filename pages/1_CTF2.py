import streamlit as st

st.set_page_config(
    page_title="Capture The Flag2",
    page_icon="🚩",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag2 - Coming Soon</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')
