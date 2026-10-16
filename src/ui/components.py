import streamlit as st


def inject_custom_css() -> None:
    """Inject custom CSS for styling."""
    st.markdown("""
    <style>
    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #dc2626 0%, #f97316 25%, #8b5cf6 50%, #3b82f6 75%, #1e3a8a 100%);
    }
    
    /* Radio buttons horizontal */
    .stRadio > div {
        flex-direction: row !important;
        gap: 1rem;
    }
    .stRadio label {
        flex: 1;
        text-align: center;
        padding: 1rem;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .stRadio label:hover {
        border-color: #3b82f6;
        background-color: #eff6ff;
    }
    .stRadio input:checked + label {
        border-color: #3b82f6;
        background-color: #dbeafe;
        font-weight: 600;
    }
    
    /* Result bar container */
    .result-bar-container {
        margin: 1rem 0;
    }
    .result-bar-label {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    .result-bar-track {
        height: 24px;
        border-radius: 12px;
        background: linear-gradient(90deg, #dc2626 0%, #f97316 25%, #8b5cf6 50%, #3b82f6 75%, #1e3a8a 100%);
        position: relative;
        overflow: hidden;
    }
    .result-bar-marker {
        position: absolute;
        top: -8px;
        width: 4px;
        height: 40px;
        background: #1f2937;
        transform: translateX(-50%);
        z-index: 10;
    }
    .result-bar-marker::before {
        content: '';
        position: absolute;
        top: 8px;
        left: -6px;
        width: 16px;
        height: 16px;
        background: #1f2937;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .result-bar-labels {
        display: flex;
        justify-content: space-between;
        margin-top: 0.5rem;
        font-size: 0.75rem;
        color: #6b7280;
    }
    
    /* Result card */
    .result-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .result-card h3 {
        margin: 0 0 1rem 0;
        font-size: 1.125rem;
        font-weight: 600;
        color: #1f2937;
    }
    .result-classification {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.875rem;
        margin-bottom: 1rem;
    }
    .classification-left { background: #dbeafe; color: #1e40af; }
    .classification-center_left { background: #e0e7ff; color: #3730a3; }
    .classification-center { background: #f3f4f6; color: #374151; }
    .classification-center_right { background: #fed7aa; color: #9a3412; }
    .classification-right { background: #fee2e2; color: #991b1b; }
    
    /* Explanation text */
    .explanation-text {
        color: #4b5563;
        line-height: 1.6;
        font-size: 0.9375rem;
    }
    
    /* Welcome page */
    .welcome-container {
        text-align: center;
        padding: 3rem 1rem;
        max-width: 700px;
        margin: 0 auto;
    }
    .welcome-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .welcome-subtitle {
        font-size: 1.125rem;
        color: #6b7280;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Language selector */
    .language-selector {
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 100;
    }
    
    /* Methodology footer */
    .methodology-footer {
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e5e7eb;
        color: #6b7280;
        font-size: 0.875rem;
        text-align: center;
    }
    
    /* Question card */
    .question-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
    }
    .question-theme {
        font-size: 0.875rem;
        font-weight: 600;
        color: #3b82f6;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
    }
    .question-text {
        font-size: 1.25rem;
        font-weight: 500;
        color: #1f2937;
        line-height: 1.5;
    }
    
    /* Navigation buttons */
    .nav-buttons {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    /* Mobile responsive */
    @media (max-width: 640px) {
        .welcome-title { font-size: 1.75rem; }
        .welcome-subtitle { font-size: 1rem; }
        .question-text { font-size: 1.125rem; }
        .stRadio > div { flex-direction: column !important; }
        .stRadio label { text-align: left; }
        .nav-buttons { flex-direction: column; }
    }
    </style>
    """, unsafe_allow_html=True)


def render_language_selector() -> None:
    """Render language selector in top right."""
    from src.core.i18n import get_available_languages, set_language, get_language
    
    langs = get_available_languages()
    current = get_language()
    
    col1, col2 = st.columns([6, 1])
    with col2:
        selected = st.selectbox(
            "🌐",
            options=langs,
            index=langs.index(current) if current in langs else 0,
            format_func=lambda x: "🇧🇷 PT" if x == "pt_BR" else "🇺🇸 EN",
            label_visibility="collapsed",
            key="lang_selector"
        )
        if selected != current:
            set_language(selected)
            st.rerun()


def render_progress_bar(current: int, total: int) -> None:
    """Render progress bar with custom text."""
    from src.core.i18n import t
    
    progress = (current) / total
    st.progress(progress)
    st.caption(t("progress_text").format(current=current + 1, total=total))


def render_question_card(question: dict, lang: str, selected: int | None) -> int | None:
    """Render a question card with radio buttons.
    
    Returns the selected value (0 or 1) or None if not changed.
    """
    from src.core.i18n import get_text
    
    st.markdown(f"""
    <div class="question-card">
        <div class="question-theme">{get_text(question["theme_key"], lang)}</div>
        <div class="question-text">{get_text(question["theme_key"], lang)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Actually show the question text, not theme twice
    st.markdown(f'<div class="question-text">{get_text(question["theme_key"], lang)}</div>', unsafe_allow_html=True)
    
    options = {
        0: get_text(question["right_key"], lang),
        1: get_text(question["left_key"], lang),
    }
    
    # Use horizontal radio
    choice = st.radio(
        label="",
        options=[0, 1],
        format_func=lambda x: options[x],
        index=None if selected is None else selected,
        horizontal=True,
        key=f"q_{question['id']}",
        label_visibility="collapsed"
    )
    
    return choice


def render_navigation_buttons(
    current: int,
    total: int,
    has_answer: bool,
    on_prev: callable,
    on_next: callable,
    on_finish: callable
) -> None:
    """Render navigation buttons."""
    from src.core.i18n import t
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if current > 0:
            if st.button(t("prev_button"), use_container_width=True, key="btn_prev"):
                on_prev()
    
    with col2:
        # Spacer
        pass
    
    with col3:
        if current < total - 1:
            if st.button(
                t("next_button"),
                use_container_width=True,
                disabled=not has_answer,
                key="btn_next",
                type="primary"
            ):
                on_next()
        else:
            if st.button(
                t("finish_button"),
                use_container_width=True,
                disabled=not has_answer,
                key="btn_finish",
                type="primary"
            ):
                on_finish()


def render_result_bar(
    scale_label: str,
    score: int,
    max_score: int,
    classification: str,
    explanation: str,
    lang: str
) -> None:
    """Render a horizontal result bar with marker and explanation."""
    from src.core.i18n import get_text
    
    # Calculate position percentage
    position_pct = (score / max_score) * 100 if max_score > 0 else 0
    
    # Classification label
    class_label = get_text(f"classification_{classification}", lang)
    
    # CSS class for classification badge
    class_css = f"classification-{classification}"
    
    st.markdown(f"""
    <div class="result-card">
        <h3>{scale_label}</h3>
        <span class="result-classification {class_css}">{class_label}</span>
        <div class="result-bar-container">
            <div class="result-bar-label">
                <span>0</span>
                <span>{max_score}</span>
            </div>
            <div class="result-bar-track">
                <div class="result-bar-marker" style="left: {position_pct}%;"></div>
            </div>
            <div class="result-bar-labels">
                <span>{get_text("classification_right", lang)}</span>
                <span>{get_text("classification_center", lang)}</span>
                <span>{get_text("classification_left", lang)}</span>
            </div>
        </div>
        <p class="explanation-text">{explanation}</p>
        <p style="color: #9ca3af; font-size: 0.875rem; margin-top: 0.5rem;">
            {get_text("result_label", lang).format(label=class_label, score=score, max=max_score)}
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_methodology_footer() -> None:
    """Render methodology footer with credits."""
    from src.core.i18n import t
    
    st.markdown(f"""
    <div class="methodology-footer">
        <p>{t("methodology_detail")}</p>
        <p><strong>{t("source_link")}</strong></p>
    </div>
    """, unsafe_allow_html=True)


def render_welcome_page() -> bool:
    """Render welcome page. Returns True if start clicked."""
    from src.core.i18n import t
    
    st.markdown(f"""
    <div class="welcome-container">
        <h1 class="welcome-title">{t("app_title")}</h1>
        <p class="welcome-subtitle">{t("app_subtitle")}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(t("start_button"), use_container_width=True, type="primary", key="btn_start"):
            return True
    
    render_methodology_footer()
    return False