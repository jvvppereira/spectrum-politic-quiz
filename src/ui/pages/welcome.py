import streamlit as st
from src.ui.components import render_welcome_page, render_language_selector, inject_custom_css
from src.utils.session import init_session_state, set_quiz_started


def render_welcome() -> None:
    """Render welcome page and handle start action."""
    inject_custom_css()
    init_session_state()
    render_language_selector()
    
    if render_welcome_page():
        from src.utils.session import reset_quiz
        reset_quiz(keep_lang=True)
        set_quiz_started(True)
        st.rerun()