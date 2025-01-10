import streamlit as st

st.set_page_config(
    page_title="Capture The Flag",
    page_icon="🚩",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')


instructions='<p style="font-family:Courier; color:Black; font-size: 20px;">Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF</b> <br>Use the commands we learned in class (ex. cd, cat, ls) to navigate and find the flags.  Enter your answers in the boxes to the right of the questions and then hit Check Answers.<br><br>Happy Hunting! (Hint: Flags look like: FLG-####)<br><br>Sometimes I do not want to give the whole file name, so I use stars in place of characters below.</p>'
st.markdown(instructions, unsafe_allow_html=True)


# Create two columns: one for the input box and the other for feedback
col1, col2 = st.columns([3, 1])  # You can adjust the width ratio as needed

with col1:
    # Input box for flag entry
    n = st.text_input("Enter the flag in file1:")

with col2:
    # Show feedback based on the user input
    if len(n) > 0:
        if n == 'FLG-123':
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;">Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;">Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
		
flag2='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in file2: </p>'
st.markdown(flag2, unsafe_allow_html=True)
flag3='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in *file3: </p>'
st.markdown(flag3, unsafe_allow_html=True)
flag4='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in file4: </p>'
st.markdown(flag4, unsafe_allow_html=True)
flag5='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in *file5: </p>'
st.markdown(flag5, unsafe_allow_html=True)
flag6='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in file6: </p>'
st.markdown(flag6, unsafe_allow_html=True)
flag7='<p style="font-family:Courier; color:White; font-size: 20px;">Enter the flag in *file7*: </p>'
st.markdown(flag7, unsafe_allow_html=True)
