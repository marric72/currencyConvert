import streamlit as st

st.set_page_config(
    page_title="Capture The Flag",
    page_icon="🚩",
)

# Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')

instructions = '<p style="font-family:Courier; color:Black; font-size: 20px;">Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF</b> <br>Use the commands we learned in class (ex. cd, cat, ls) to navigate and find the flags. Enter your answers in the boxes to the right of the questions and then hit Check Answers.<br><br>Happy Hunting! (Hint: Flags look like: FLG-###)<br><br>Sometimes I do not want to give the whole filename, so I use stars in place of characters below.</p>'
st.markdown(instructions, unsafe_allow_html=True)

# Create three columns: one for the question, one for the input box, and one for feedback
questions = [
    ("Enter the flag in file1:", "FLG-123"),
    ("Enter the flag in file2:", "FLG-444"),
    ("Enter the flag in *file3:", "FLG-936"),
    ("Enter the flag in file4:", "FLG-045"),
    ("Enter the flag in file5:", "FLG-246"),
    ("Enter the flag in file6:", "FLG-135"),
    ("Enter the flag in *file7*:", "FLG-765")
]

for question, correct_flag in questions:
    col1, col2, col3 = st.columns([3, 2, 2])  # Adjust column widths as needed

    with col1:
        st.write(question)  # Display the question
    
    with col2:
        # Input box for the flag entry
        user_input = st.text_input(f"Your answer for {question}", key=question)

    with col3:
        # Provide feedback based on the user input
        if len(user_input) > 0:
            if user_input == correct_flag:
                feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;">Correct!</p>'
                st.markdown(feedback, unsafe_allow_html=True)
            else:
                feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;">Incorrect</p>'
                st.markdown(feedback, unsafe_allow_html=True)
