import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Political Spectrum Quiz",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state early
from src.utils.session import init_session_state
init_session_state()

# Route to appropriate page
from src.utils.session import is_quiz_completed, is_quiz_started

if is_quiz_completed():
    from src.ui.pages.results import render_results
    render_results()
elif is_quiz_started():
    from src.ui.pages.quiz import render_quiz
    render_quiz()
else:
    from src.ui.pages.welcome import render_welcome
    render_welcome()