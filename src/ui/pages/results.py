import streamlit as st
from src.core.i18n import get_language, get_text, t
from src.ui.components import (
    render_result_bar,
    render_language_selector,
    render_methodology_footer,
    inject_custom_css
)
from src.utils.session import (
    init_session_state,
    get_results,
    is_quiz_completed,
    reset_quiz
)


def render_results() -> None:
    """Render results page with three scales."""
    inject_custom_css()
    init_session_state()
    render_language_selector()
    
    if not is_quiz_completed():
        st.switch_page("src/ui/pages/quiz.py")
        return
    
    results = get_results()
    if not results:
        st.switch_page("src/ui/pages/welcome.py")
        return
    
    lang = get_language()
    
    # Title
    st.markdown(f"""
    <div class="welcome-container">
        <h1 class="welcome-title">{t("app_title")}</h1>
        <p class="welcome-subtitle">{t("app_subtitle")}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Behavioral scale
    behavioral_class = results["behavioral_classification"]
    render_result_bar(
        scale_label=t("scale_behavioral"),
        score=results["behavioral_score"],
        max_score=results["behavioral_max"],
        classification=behavioral_class,
        explanation=get_text(
            f"explanation_behavioral_{behavioral_class}", lang
        ),
        lang=lang
    )
    
    # Economic scale
    economic_class = results["economic_classification"]
    render_result_bar(
        scale_label=t("scale_economic"),
        score=results["economic_score"],
        max_score=results["economic_max"],
        classification=economic_class,
        explanation=get_text(
            f"explanation_economic_{economic_class}", lang
        ),
        lang=lang
    )
    
    # General scale
    general_class = results["general_classification"]
    render_result_bar(
        scale_label=t("scale_general"),
        score=results["general_score"],
        max_score=results["general_max"],
        classification=general_class,
        explanation=get_text(
            f"explanation_general_{general_class}", lang
        ),
        lang=lang
    )
    
    # Restart button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(t("restart_button"), use_container_width=True, type="primary", key="btn_restart"):
            reset_quiz(keep_lang=True)
            st.rerun()
    
    render_methodology_footer()