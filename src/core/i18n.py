import json
from pathlib import Path
from typing import Dict, Optional

_locale_cache: Dict[str, Dict[str, str]] = {}
_available_languages: Optional[list] = None


def load_locale(lang: str) -> Dict[str, str]:
    """Load locale JSON file with caching."""
    if lang in _locale_cache:
        return _locale_cache[lang]
    
    locale_path = Path(__file__).parent.parent.parent / "locales" / f"{lang}.json"
    
    if not locale_path.exists():
        lang = "pt_BR"
        locale_path = Path(__file__).parent.parent.parent / "locales" / f"{lang}.json"
    
    with open(locale_path, "r", encoding="utf-8") as f:
        locale_data = json.load(f)
    
    _locale_cache[lang] = locale_data
    return locale_data


def get_text(key: str, lang: str = "pt_BR") -> str:
    """Get translated text for a key with fallback to pt_BR."""
    locale = load_locale(lang)
    if key in locale:
        return locale[key]
    
    # Fallback to pt_BR
    if lang != "pt_BR":
        pt_locale = load_locale("pt_BR")
        if key in pt_locale:
            return pt_locale[key]
    
    return key


def get_available_languages() -> list:
    """Get list of available language codes."""
    global _available_languages
    if _available_languages is None:
        locales_dir = Path(__file__).parent.parent.parent / "locales"
        _available_languages = [
            f.stem for f in locales_dir.glob("*.json")
        ]
    return _available_languages


def init_i18n() -> str:
    """Initialize i18n in session state. Returns current language."""
    import streamlit as st
    
    if "lang" not in st.session_state:
        st.session_state.lang = "pt_BR"
    
    return st.session_state.lang


def set_language(lang: str) -> None:
    """Set current language in session state."""
    import streamlit as st
    
    if lang in get_available_languages():
        st.session_state.lang = lang


def get_language() -> str:
    """Get current language from session state."""
    import streamlit as st
    return st.session_state.get("lang", "pt_BR")


def t(key: str) -> str:
    """Shorthand for get_text using current session language."""
    return get_text(key, get_language())