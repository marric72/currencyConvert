import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Prescott Cowboy Adventure",
    page_icon="🤠",
    layout="centered"
)

# Session state
if "avatar" not in st.session_state:
    st.session_state.avatar = "teddy.png"

if "page" not in st.session_state:
    st.session_state.page = "Home"


# Navigation
st.sidebar.title("🤠 Cowboy Menu")

choice = st.sidebar.radio(
    "Choose Adventure",
    [
        "Select Avatar",
        "Prescott Trivia",
        "Cowboy Roundup Game"
    ]
)


# Avatar Page
if choice == "Select Avatar":

    st.header("Choose Your Cowboy")

    avatar = st.radio(
        "Select Avatar",
        [
            "Theodore Roosevelt",
            "Annie Oakley",
            "Wyatt Earp"
        ]
    )

    if avatar == "Theodore Roosevelt":
        st.session_state.avatar = "teddy.png"

    elif avatar == "Annie Oakley":
        st.session_state.avatar = "annie.png"

    elif avatar == "Wyatt Earp":
        st.session_state.avatar = "wyatt.png"


    st.image(
        st.session_state.avatar,
        width=250
    )


# Trivia Page
elif choice == "Prescott Trivia":

    st.header("🤠 Prescott Trivia")

    questions = {
        "Prescott was Arizona's first territorial capital.": 
            ["True", "False"],

        "What famous street is known for historic saloons?":
            ["Whiskey Row", "Main Street", "Gold Street"],

        "Which lake is near Prescott?":
            ["Watson Lake", "Roosevelt Lake", "Lake Pleasant"],

        "Which forest surrounds Prescott?":
            ["Prescott National Forest",
             "Coconino National Forest"],

        "Prescott's famous rodeo is called:":
            ["World's Oldest Rodeo",
             "Arizona Stampede"]
    }

    answers = [
        "True",
        "Whiskey Row",
        "Watson Lake",
        "Prescott National Forest",
        "World's Oldest Rodeo"
    ]

    user_answers=[]

    for q, options in questions.items():

        user_answers.append(
            st.radio(q, options)
        )


    if st.button("Submit Quiz"):

        score=0

        for user, correct in zip(user_answers, answers):
            if user == correct:
                score += 1

        st.success(
            f"You scored {score}/5!"
        )


# Cowboy Game
elif choice == "Cowboy Roundup Game":

    st.header("🐎 Cowboy Roundup")

    components.html(
        """
        <div id="game">
        <h2>Round up the horses!</h2>
        <p>Game version goes here.</p>
        </div>
        """,
        height=600
    )
