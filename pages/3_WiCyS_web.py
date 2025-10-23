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
title = '<p style="font-family:Courier; color:White; font-size: 30px;">Top Secret Website</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("computer.png", caption=' ')

instructions = '<p style="font-family:Courier; color:Yellow; font-size: 20px;">Login to find the flag.</p>'
st.markdown(instructions, unsafe_allow_html=True)

# Define the correct credentials
correct_username = "Heather"
correct_password = "password"

# Create columns for username and password input
col1, col2 = st.columns([1, 3])

# Username input
with col1:
    st.markdown('<p style="font-family:Courier; color:White; font-size: 20px;">Username:</p>', unsafe_allow_html=True)
    username = st.text_input("", key="username")

# Password input
with col2:
    st.markdown('<p style="font-family:Courier; color:White; font-size: 20px;">Password:</p>', unsafe_allow_html=True)
    password = st.text_input("", type="password", key="password")

# Login button
if st.button("Login"):
    if username == correct_username and password == correct_password:
        st.success("Congratulations! You've logged in successfully. FLG_LOGN-3698")
    else:
        st.error("Incorrect username or password. Please try again.")

# Custom horizontal line
line = f'<hr>'
st.markdown(line, unsafe_allow_html=True)

