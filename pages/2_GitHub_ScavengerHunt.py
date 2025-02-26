import streamlit as st

st.set_page_config(
    page_title="Scavenger Hunt",
    page_icon="🔍",
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
title = '<p style="font-family:Courier; color:White; font-size: 30px;">GitHub Scavenger Hunt</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')

instructions = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">Use this link for the scavenger hunt: <a href="https://github.com/marric72/ScavengerHunt">https://github.com/marric72/ScavengerHunt</a> <br></p>'
st.markdown(instructions, unsafe_allow_html=True)

# Create three columns: one for the question, one for the input box, and one for feedback
questions = [
    ("What is the name of the repo? ", "ScavengerHunt"),
    ("What is the repo author's name? ", "marric72"),
    ("What will print when hello.cpp is compiled and run? ", "Hello Class."),
    ("What did the original version of hello.cpp print? ", "Hello World!"),
    ("How many time was hello.cpp updated? ", "3"),
    ("How many branches are there? ", "2"),
    ("What comment did m8rmclaren make on the latest pull request? ", "Nice addition!"),
    ("What is the name of the deleted file? ", "wordsOfWisdom"),
     ("To clone this repo, type: git clone _______ ", "https://github.com/marric72/ScavengerHunt.git")
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
