import streamlit as st
from src.core.questions import QUESTIONS
from src.core.i18n import get_language, t
from src.ui.components import (
    render_progress_bar,
    render_question_card,
    render_navigation_buttons,
    render_language_selector,
    inject_custom_css
)
from src.utils.session import (
    init_session_state,
    get_current_question_index,
    set_current_question_index,
    get_answer,
    set_answer,
    is_quiz_completed,
    can_go_next,
    can_go_prev,
    is_last_question
)


def render_quiz() -> None:
    """Render quiz page with paginated questions."""
    inject_custom_css()
    init_session_state()
    render_language_selector()
    
    if is_quiz_completed():
        st.switch_page("src/ui/pages/results.py")
        return
    
    lang = get_language()
    current_idx = get_current_question_index()
    total = len(QUESTIONS)
    question = QUESTIONS[current_idx]
    qid = question["id"]
    
    # Render progress
    render_progress_bar(current_idx, total)
    
    # Get current answer
    current_answer = get_answer(qid)
    
    # Render question
    choice = render_question_card(question, lang, current_answer)
    
    # Handle answer change
    if choice is not None and choice != current_answer:
        set_answer(qid, choice)
        st.rerun()
    
    # Navigation callbacks
    def on_prev():
        if can_go_prev():
            set_current_question_index(current_idx - 1)
            st.rerun()
    
    def on_next():
        if can_go_next(total):
            set_current_question_index(current_idx + 1)
            st.rerun()
    
    def on_finish():
        from src.core.scoring import calculate_all_scores
        from src.utils.session import set_quiz_completed, set_results, get_all_answers
        
        answers = get_all_answers()
        results = calculate_all_scores(answers)
        set_results(results)
        set_quiz_completed(True)
        st.rerun()
    
    # Render navigation
    has_answer = current_answer is not None
    render_navigation_buttons(
        current=current_idx,
        total=total,
        has_answer=has_answer,
        on_prev=on_prev,
        on_next=on_next,
        on_finish=on_finish
    )