import streamlit as st

st.set_page_config(
    page_title="Capture The Flag",
    page_icon="🚩",
)

# Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')

instructions = '<p style="font-family:Courier; color:Black; font-size: 20px;">Use Linux command line only. <br> Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF</b> <br>Use the commands we learned in class (ex. cd, cat, ls) to navigate and find the flags. Enter your answers in the boxes to the right of the questions and then hit Check Answers.<br><br>Happy Hunting! (Hint: Flags look like: FLG-###)<br><br>Sometimes I do not want to give the whole filename, so I use stars in place of characters below.</p>'
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
# Adding custom CSS to put lines around each row
css = """
    <style>
        .row {
            border: 1px solid black;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
        }
        .column {
            padding: 10px;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

for question, correct_flag in questions:
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column widths as needed
# Add the CSS class 'row' to each row for styling
    with col1:
        st.markdown(f'<div class="row"><div class="column"><br>{question}</div>', unsafe_allow_html=True)
    
    #with col1:
    #    feedback = f'<p style="font-family:Courier; color:White; font-size: 20px;"><br>{question}</p>'
    #    st.markdown(feedback, unsafe_allow_html=True)
    
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
# Close the div tag for row styling
        st.markdown('</div></div>', unsafe_allow_html=True)
