import streamlit as st
from typing import Dict, Any, Optional


def _get_state() -> Dict[str, Any]:
    """Get session state as dict (works with both real and mocked)."""
    if hasattr(st.session_state, '__dict__'):
        return st.session_state
    return st.session_state


def init_session_state() -> None:
    """Initialize all session state variables."""
    state = _get_state()
    defaults = {
        "lang": "pt_BR",
        "current_question": 0,
        "answers": {},
        "quiz_completed": False,
        "results": None,
        "quiz_started": False,
    }
    
    for key, value in defaults.items():
        if key not in state:
            state[key] = value


def reset_quiz(keep_lang: bool = True) -> None:
    """Reset quiz state, optionally keeping language."""
    state = _get_state()
    lang = state.get("lang", "pt_BR") if keep_lang else "pt_BR"
    
    state["current_question"] = 0
    state["answers"] = {}
    state["quiz_completed"] = False
    state["results"] = None
    state["lang"] = lang
    state["quiz_started"] = False


def get_current_question_index() -> int:
    """Get current question index (0-based)."""
    state = _get_state()
    return state.get("current_question", 0)


def set_current_question_index(index: int) -> None:
    """Set current question index."""
    state = _get_state()
    state["current_question"] = index


def get_answer(question_id: int) -> Optional[int]:
    """Get answer for a question (0 or 1)."""
    state = _get_state()
    return state.get("answers", {}).get(question_id)


def set_answer(question_id: int, value: int) -> None:
    """Set answer for a question."""
    state = _get_state()
    if "answers" not in state:
        state["answers"] = {}
    state["answers"][question_id] = value


def get_all_answers() -> Dict[int, int]:
    """Get all answers."""
    state = _get_state()
    return state.get("answers", {}).copy()


def is_quiz_completed() -> bool:
    """Check if quiz is completed."""
    state = _get_state()
    return state.get("quiz_completed", False)


def set_quiz_completed(completed: bool = True) -> None:
    """Mark quiz as completed."""
    state = _get_state()
    state["quiz_completed"] = completed


def is_quiz_started() -> bool:
    """Check if quiz has started."""
    state = _get_state()
    return state.get("quiz_started", False)


def set_quiz_started(started: bool = True) -> None:
    """Mark quiz as started."""
    state = _get_state()
    state["quiz_started"] = started


def set_results(results: Dict[str, Any]) -> None:
    """Store calculated results."""
    state = _get_state()
    state["results"] = results


def get_results() -> Optional[Dict[str, Any]]:
    """Get stored results."""
    state = _get_state()
    return state.get("results")


def get_language() -> str:
    """Get current language."""
    state = _get_state()
    return state.get("lang", "pt_BR")


def set_language(lang: str) -> None:
    """Set current language."""
    state = _get_state()
    state["lang"] = lang


def can_go_next(total_questions: int) -> bool:
    """Check if can go to next question."""
    current = get_current_question_index()
    if current >= total_questions - 1:
        return False
    # Check if current question is answered
    from src.core.questions import QUESTIONS
    qid = QUESTIONS[current]["id"]
    return get_answer(qid) is not None


def can_go_prev() -> bool:
    """Check if can go to previous question."""
    return get_current_question_index() > 0


def is_last_question(total_questions: int) -> bool:
    """Check if on last question."""
    return get_current_question_index() >= total_questions - 1