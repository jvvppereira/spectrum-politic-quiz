from typing import Dict
from .questions import (
    BEHAVIORAL_QUESTION_IDS,
    ECONOMIC_QUESTION_IDS,
    BEHAVIORAL_THRESHOLDS,
    ECONOMIC_THRESHOLDS,
    GENERAL_THRESHOLDS,
    CLASSIFICATION_KEYS,
    MAX_BEHAVIORAL,
    MAX_ECONOMIC,
    MAX_GENERAL,
)


def calculate_behavioral_score(answers: Dict[int, int]) -> int:
    """Calculate behavioral scale score (0-10).
    
    Args:
        answers: Dict mapping question_id -> 0 (right) or 1 (left)
    
    Returns:
        Sum of left answers for behavioral questions (0-10)
    """
    score = 0
    for qid in BEHAVIORAL_QUESTION_IDS:
        if answers.get(qid) == 1:
            score += 1
    return score


def calculate_economic_score(answers: Dict[int, int]) -> int:
    """Calculate economic scale score (0-6).
    
    Args:
        answers: Dict mapping question_id -> 0 (right) or 1 (left)
    
    Returns:
        Sum of left answers for economic questions (0-6)
    """
    score = 0
    for qid in ECONOMIC_QUESTION_IDS:
        if answers.get(qid) == 1:
            score += 1
    return score


def calculate_general_score(behavioral_score: int, economic_score: int) -> int:
    """Calculate general scale score (0-12) using Datafolha weighted method.
    
    Behavioral (0-10) is normalized to 0-6: behavioral_score * 6 / 10
    Economic (0-6) stays as is.
    General = normalized_behavioral + economic (0-12)
    
    Args:
        behavioral_score: Score from behavioral scale (0-10)
        economic_score: Score from economic scale (0-6)
    
    Returns:
        General score rounded to nearest integer (0-12)
    """
    normalized_behavioral = behavioral_score * 6 / 10
    general = normalized_behavioral + economic_score
    return round(general)


def classify_score(score: int, scale_type: str) -> str:
    """Classify a score into ideological category.
    
    Args:
        score: The score to classify
        scale_type: One of "behavioral", "economic", "general"
    
    Returns:
        Classification key: "left", "center_left", "center", "center_right", "right"
    """
    if scale_type == "behavioral":
        thresholds = BEHAVIORAL_THRESHOLDS
    elif scale_type == "economic":
        thresholds = ECONOMIC_THRESHOLDS
    elif scale_type == "general":
        thresholds = GENERAL_THRESHOLDS
    else:
        raise ValueError(f"Unknown scale_type: {scale_type}")
    
    for classification in CLASSIFICATION_KEYS:
        min_score, max_score = thresholds[classification]
        if min_score <= score <= max_score:
            return classification
    
    return "center"


def get_scale_label(classification: str, lang: str, i18n_get_text) -> str:
    """Get translated label for a classification.
    
    Args:
        classification: Classification key
        lang: Language code (pt_BR, en_US)
        i18n_get_text: Function to get translated text
    
    Returns:
        Translated label
    """
    from .questions import SCALE_LABELS_KEYS
    label_key = SCALE_LABELS_KEYS.get(classification, "classification_center")
    return i18n_get_text(label_key, lang)


def get_explanation(classification: str, scale_type: str, lang: str, i18n_get_text) -> str:
    """Get translated explanation for a classification and scale.
    
    Args:
        classification: Classification key
        scale_type: One of "behavioral", "economic", "general"
        lang: Language code
        i18n_get_text: Function to get translated text
    
    Returns:
        Translated explanation text
    """
    from .questions import EXPLANATION_KEYS
    exp_key = EXPLANATION_KEYS.get(scale_type, {}).get(classification)
    if exp_key:
        return i18n_get_text(exp_key, lang)
    return ""


def calculate_all_scores(answers: Dict[int, int]) -> Dict[str, any]:
    """Calculate all three scores and classifications.
    
    Args:
        answers: Dict mapping question_id -> 0 (right) or 1 (left)
    
    Returns:
        Dict with scores, classifications, and max values
    """
    behavioral = calculate_behavioral_score(answers)
    economic = calculate_economic_score(answers)
    general = calculate_general_score(behavioral, economic)
    
    return {
        "behavioral_score": behavioral,
        "behavioral_max": MAX_BEHAVIORAL,
        "behavioral_classification": classify_score(behavioral, "behavioral"),
        "economic_score": economic,
        "economic_max": MAX_ECONOMIC,
        "economic_classification": classify_score(economic, "economic"),
        "general_score": general,
        "general_max": MAX_GENERAL,
        "general_classification": classify_score(general, "general"),
    }