import streamlit as st

st.set_page_config(
    page_title="Login Exercise",
    page_icon="💻",
)
# Add custom CSS for the <hr> tag
st.markdown("""
    <style>
        hr {
            border: 0;
            height: 2px;
            background-color: #000000; /* Change to any color you prefer */
            width: 50%;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')

instructions = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">Use Linux commands to find the flags. <br> Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF2</b> <br>Enter your answers in the boxes to the right of the questions and then hit Enter.<br><br>Happy Hunting! (Hint: Flags look like: FLG-####)</p>'
st.markdown(instructions, unsafe_allow_html=True)

# Create three columns: one for the question, one for the input box, and one for feedback
questions = [
    ("Login:", "Heather"),
    ("Password:", "password")
]
# Adding custom CSS to put lines around each row


for question, correct_flag in questions:
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column widths as needed
    
    with col1:
        feedback = f'<p style="font-family:Courier; color:White; font-size: 20px;"><br>{question}</p>'
        st.markdown(feedback, unsafe_allow_html=True)
    
    with col2:
        # Input box for the flag entry
        user_input = st.text_input(f" ", key=question)

    with col3:
        # Provide feedback based on the user input
        if len(user_input) > 0:
            if user_input == correct_flag:
                feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
                st.markdown(feedback, unsafe_allow_html=True)
            else:
                feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
                st.markdown(feedback, unsafe_allow_html=True)
    line=f'<hr>'
    st.markdown(line, unsafe_allow_html=True)
