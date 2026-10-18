
import random
import streamlit as st

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = "I'm thinking of a number... 💗"

st.title("🎮 Number Guessing Game")
st.write("Guess the number between 1 and 100!")

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("✨ Guess", use_container_width=True):
    if not st.session_state.finished:
        st.session_state.attempts += 1

        if guess == st.session_state.number:
            st.session_state.message = (
                f"🎉 Correct! You won in "
                f"{st.session_state.attempts} attempts!"
            )
            st.session_state.finished = True
            st.balloons()

        elif guess < st.session_state.number:
            st.session_state.message = "⬆️ Too low! Try a higher number."

        else:
            st.session_state.message = "⬇️ Too high! Try a lower number."

st.info(st.session_state.message)
st.write(f"**Attempts:** {st.session_state.attempts}")

if st.button("🔄 New Game", use_container_width=True):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = "I'm thinking of a new number... 💗"
    st.rerun()
