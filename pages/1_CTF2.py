import streamlit as st

st.set_page_config(
    page_title="Capture The Flag2",
    page_icon="🚩",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:White; font-size: 30px;">prclab1 Capture the Flag2 </p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')


instructions='<p style="font-family:Courier; color:Black; font-size: 20px;">Start on <b>prclab1</b> in the directory<br> <b>/home/faculty/marric72/cs125_CTF2</b> <br>Use the commands we learned in class to navigate and find the flags.  In some cases, it will be easier to COPY my C programs to your directory so you can compile and run. <br><br>Enter your answers below.  Remember the flag format is FLG-####</p>'
st.markdown(instructions, unsafe_allow_html=True)


# Create two columns: one for the input box and the other for feedback
col1, col2 = st.columns([3, 1])  # You can adjust the width ratio as needed

with col1:
    # Input box for flag entry
    n = st.text_input("Freebee: Enter FLG-0123:")

with col2:
    # Show feedback based on the user input
    if len(n) > 0:
        if n == 'FLG-0123':
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)


# Create two columns: one for the input box and the other for feedback
col1, col2 = st.columns([3, 1])  # You can adjust the width ratio as needed

with col1:
    # Input box for flag entry
    n = st.text_input("Enter the flag in file0:")

with col2:
    # Show feedback based on the user input
    if len(n) > 0:
        if n == 'FLG-1010':
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
		
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag2 entry
    n2 = st.text_input("Enter the flag in file1(warning: this is too big to open, do NOT use nano):")

#FLAG 2
with col2:
    # Show feedback for file2
    if len(n2) > 0:
        if n2 == 'FLG-1111':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag3 entry
    n2 = st.text_input("The flag is the only difference between file1 and file2:")

with col2:
    # Show feedback for file3
    if len(n2) > 0:
        if n2 == 'FLG-1313':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
# Create two columns: one for the input box and the other for feedback
col1, col2 = st.columns([3, 1])  # You can adjust the width ratio as needed

with col1:
    # Input box for flag entry
    n = st.text_input("Run switchFlag.c with correct input to generate a flag:")

with col2:
    # Show feedback based on the user input
    if len(n) > 0:
        if n == 'FLG-3344':
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
		
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag4 entry
    n2 = st.text_input("Run whileLoopFlag.c to generate a flag:")

with col2:
    # Show feedback for file5
    if len(n2) > 0:
        if n2 == 'FLG-7654':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("Run doWhileLoopFlag.c to generate the flag:")

with col2:
    # Show feedback for file3
    if len(n2) > 0:
        if n2 == 'FLG-1234':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("Run forLoopFlag.c with the correct input to generate a flag:")

with col2:
    # Show feedback for file7
    if len(n2) > 0:
        if n2 == 'FLG-5521':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("Get line 125 from lotsOfFlags.txt:")

with col2:
    # Show feedback for file7
    if len(n2) > 0:
        if n2 == 'FLG-8097':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("If sorted alphabetically, this flag is the last in flag.txt:")

with col2:
    # Show feedback for file7
    if len(n2) > 0:
        if n2 == 'FLG-9997':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("Enter the flag in file3:")

with col2:
    # Show feedback for file7
    if len(n2) > 0:
        if n2 == 'FLG-6543':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])  # Adjust column ratio as needed
with col1:
    # Input box for flag6 entry
    n2 = st.text_input("Compile and run donut.c (with gcc -lm donut.c):")

with col2:
    # Show feedback for file7
    if len(n2) > 0:
        if n2 == 'FLG-1019':  
            feedback = f'<p style="font-family:Courier; color:Green; font-size: 20px;"><br>Correct!</p>'
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            feedback = f'<p style="font-family:Courier; color:Red; font-size: 20px;"><br>Incorrect</p>'
            st.markdown(feedback, unsafe_allow_html=True)


