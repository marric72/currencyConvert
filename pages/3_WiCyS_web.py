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
            background-color: #000000;
            width: 50%;
            margin: 20px 0;
        }
        /* Change button color */
        div.stButton > button:first-child {
            background-color: #FF4B4B; /* Red color */
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-family: Courier, monospace;
            transition: all 0.3s ease;
        }

        /* Hover effect */
        div.stButton > button:first-child:hover {
            background-color: #FF1C1C;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Title and image
st.markdown('<p style="font-family:Courier; color:White; font-size: 30px;">Top Secret Website</p>', unsafe_allow_html=True)
st.image("computer.png", caption=' ')
st.markdown('<p style="font-family:Courier; color:Yellow; font-size: 20px;">Login to find the flag.</p>', unsafe_allow_html=True)

# Define the correct credentials
correct_username = "Heather"
correct_password = "password"

# Create layout with two columns: labels on the left, inputs on the right
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<p style="font-family:Courier; color:White; font-size: 20px;">Username:</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:Courier; color:White; font-size: 20px;">Password:</p>', unsafe_allow_html=True)

with col2:
    username = st.text_input("Username", label_visibility="collapsed", key="username")
    password = st.text_input("Password", label_visibility="collapsed", type="password", key="password")

# Add login button centered
st.write("")
login_button = st.button("Login")
st.title("Button Example")
# Create a button with the label "Click me!"
if st.button("Click me!"):
    st.write("The button was clicked!")
else:
    st.write("The button has not been clicked yet.")


# Login logic
if login_button:
    if username == correct_username and password == correct_password:
        st.success("🎉 Congratulations! You've logged in successfully.  FLG-LOGN-3926")
    else:
        st.error("❌ Incorrect username or password. Please try again.")

# Horizontal divider
st.markdown("<hr>", unsafe_allow_html=True)

