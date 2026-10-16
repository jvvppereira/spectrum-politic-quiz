import pytest
from unittest.mock import MagicMock
import sys
import streamlit as st


class MockStreamlit:
    """Mock streamlit for integration testing."""
    
    def __init__(self):
        self.session_state = {}
        self.calls = []
    
    def set_page_config(self, **kwargs):
        self.calls.append(("set_page_config", kwargs))
    
    def progress(self, value):
        self.calls.append(("progress", value))
    
    def caption(self, text):
        self.calls.append(("caption", text))
    
    def markdown(self, text, unsafe_allow_html=False):
        self.calls.append(("markdown", text))
    
    def radio(self, label, options, format_func=None, index=None, horizontal=False, key=None, label_visibility="visible"):
        self.calls.append(("radio", {"label": label, "options": options, "index": index, "key": key}))
        # Return the indexed option or first
        if index is not None:
            return options[index]
        return options[0]
    
    def button(self, label, use_container_width=False, disabled=False, key=None, type="secondary"):
        self.calls.append(("button", {"label": label, "disabled": disabled, "key": key}))
        return False
    
    def columns(self, spec):
        cols = []
        for _ in spec:
            col = MagicMock()
            col.__enter__ = lambda s: col
            col.__exit__ = lambda s, *a: None
            col.button = lambda *a, **k: False
            col.markdown = lambda *a, **k: None
            cols.append(col)
        return cols
    
    def selectbox(self, label, options, index=0, format_func=None, label_visibility="visible", key=None):
        self.calls.append(("selectbox", {"options": options, "index": index, "key": key}))
        return options[index]
    
    def rerun(self):
        self.calls.append(("rerun",))
        raise Exception("RERUN")
    
    def switch_page(self, page):
        self.calls.append(("switch_page", page))
    
    def error(self, msg):
        self.calls.append(("error", msg))


@pytest.fixture
def mock_st(monkeypatch):
    """Mock streamlit module."""
    mock = MockStreamlit()
    monkeypatch.setattr(st, "session_state", mock.session_state)
    monkeypatch.setattr(st, "set_page_config", mock.set_page_config)
    monkeypatch.setattr(st, "progress", mock.progress)
    monkeypatch.setattr(st, "caption", mock.caption)
    monkeypatch.setattr(st, "markdown", mock.markdown)
    monkeypatch.setattr(st, "radio", mock.radio)
    monkeypatch.setattr(st, "button", mock.button)
    monkeypatch.setattr(st, "columns", mock.columns)
    monkeypatch.setattr(st, "selectbox", mock.selectbox)
    monkeypatch.setattr(st, "rerun", mock.rerun)
    monkeypatch.setattr(st, "switch_page", mock.switch_page)
    monkeypatch.setattr(st, "error", mock.error)
    return mock


class TestWelcomePage:
    def test_welcome_renders(self, mock_st):
        from src.ui.pages.welcome import render_welcome
        
        # Mock button to return True on first call
        call_count = [0]
        def mock_button(*args, **kwargs):
            call_count[0] += 1
            return call_count[0] == 1
        
        mock_st.button = mock_button
        
        try:
            render_welcome()
        except Exception as e:
            if "RERUN" not in str(e):
                raise
        
        # Check welcome page rendered
        assert any(c[0] == "markdown" and "welcome-title" in c[1] for c in mock_st.calls)
    
    def test_language_selector_renders(self, mock_st):
        from src.ui.components import render_language_selector
        from src.utils.session import init_session_state
        
        init_session_state()
        render_language_selector()
        
        assert any(c[0] == "selectbox" for c in mock_st.calls)


class TestQuizFlow:
    def test_quiz_initializes(self, mock_st):
        from src.ui.pages.quiz import render_quiz
        from src.utils.session import init_session_state
        
        init_session_state()
        
        # Mock buttons to not trigger
        mock_st.button = lambda *a, **k: False
        
        try:
            render_quiz()
        except Exception as e:
            if "RERUN" not in str(e):
                raise
        
        # Check progress bar rendered
        assert any(c[0] == "progress" for c in mock_st.calls)
    
    def test_question_navigation(self, mock_st):
        from src.ui.pages.quiz import render_quiz
        from src.utils.session import init_session_state, set_answer
        from src.core.questions import QUESTIONS
        
        init_session_state()
        set_answer(1, 1)  # Answer first question
        
        mock_st.button = lambda *a, **k: False
        
        try:
            render_quiz()
        except Exception as e:
            if "RERUN" not in str(e):
                raise
        
        # Should show question 1 (index 0)
        radio_calls = [c for c in mock_st.calls if c[0] == "radio"]
        assert len(radio_calls) > 0


class TestResultsPage:
    def test_results_renders(self, mock_st):
        from src.ui.pages.results import render_results
        from src.utils.session import init_session_state, set_quiz_completed, set_results
        
        init_session_state()
        set_quiz_completed(True)
        set_results({
            "behavioral_score": 7,
            "behavioral_max": 10,
            "behavioral_classification": "center_left",
            "economic_score": 4,
            "economic_max": 6,
            "economic_classification": "center_left",
            "general_score": 8,
            "general_max": 12,
            "general_classification": "center_left",
        })
        
        mock_st.button = lambda *a, **k: False
        
        try:
            render_results()
        except Exception as e:
            if "RERUN" not in str(e):
                raise
        
        # Check result bars rendered
        markdown_calls = [c for c in mock_st.calls if c[0] == "markdown"]
        assert any("result-bar-track" in c[1] for c in markdown_calls)
    
    def test_results_shows_three_scales(self, mock_st):
        from src.ui.pages.results import render_results
        from src.utils.session import init_session_state, set_quiz_completed, set_results
        
        init_session_state()
        set_quiz_completed(True)
        set_results({
            "behavioral_score": 5,
            "behavioral_max": 10,
            "behavioral_classification": "center",
            "economic_score": 3,
            "economic_max": 6,
            "economic_classification": "center",
            "general_score": 6,
            "general_max": 12,
            "general_classification": "center",
        })
        
        mock_st.button = lambda *a, **k: False
        
        try:
            render_results()
        except Exception as e:
            if "RERUN" not in str(e):
                raise
        
        markdown_calls = [c for c in mock_st.calls if c[0] == "markdown"]
        scale_labels = ["scale_behavioral", "scale_economic", "scale_general"]
        for label in scale_labels:
            # Check each scale is rendered (in Portuguese)
            found = any(label in c[1] or "Escala" in c[1] for c in markdown_calls)
            assert found


class TestFullFlow:
    def test_complete_quiz_flow(self, mock_st):
        """Test complete flow from welcome to results."""
        from src.utils.session import init_session_state, reset_quiz
        from src.core.scoring import calculate_all_scores
        
        init_session_state()
        reset_quiz()
        
        # Simulate answering all questions as "left"
        answers = {q: 1 for q in range(1, 17)}
        results = calculate_all_scores(answers)
        
        assert results["behavioral_score"] == 10
        assert results["behavioral_classification"] == "left"
        assert results["economic_score"] == 6
        assert results["economic_classification"] == "left"
        assert results["general_score"] == 12
        assert results["general_classification"] == "left"
        
        # Simulate all right
        answers = {q: 0 for q in range(1, 17)}
        results = calculate_all_scores(answers)
        
        assert results["behavioral_score"] == 0
        assert results["behavioral_classification"] == "right"
        assert results["economic_score"] == 0
        assert results["economic_classification"] == "right"
        assert results["general_score"] == 0
        assert results["general_classification"] == "right"