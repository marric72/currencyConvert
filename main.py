import streamlit as st

st.set_page_config(
    page_title="Capture The Flag2",
    page_icon="🚩",
)

#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag2 - COMING SOON </p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')


instructions='<p style="font-family:Courier; color:Black; font-size: 20px;">Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF2</b> <br>Use the commands we learned in class to navigate and find the flags.  In some cases, it will be easier to COPY my C programs to your directory so you can compile and run. <br><br>Enter your answers below.  The flag format is FLG-####</p>'
st.markdown(instructions, unsafe_allow_html=True)

