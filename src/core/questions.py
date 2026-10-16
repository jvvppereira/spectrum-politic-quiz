from typing import List, Dict, Any

QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "theme_key": "q1_theme",
        "scale": "economic",
        "left_key": "q1_left",
        "right_key": "q1_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 2,
        "theme_key": "q2_theme",
        "scale": "economic",
        "left_key": "q2_left",
        "right_key": "q2_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 3,
        "theme_key": "q3_theme",
        "scale": "economic",
        "left_key": "q3_left",
        "right_key": "q3_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 4,
        "theme_key": "q4_theme",
        "scale": "economic",
        "left_key": "q4_left",
        "right_key": "q4_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 5,
        "theme_key": "q5_theme",
        "scale": "economic",
        "left_key": "q5_left",
        "right_key": "q5_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 6,
        "theme_key": "q6_theme",
        "scale": "economic",
        "left_key": "q6_left",
        "right_key": "q6_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 7,
        "theme_key": "q7_theme",
        "scale": "behavioral",
        "left_key": "q7_left",
        "right_key": "q7_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 8,
        "theme_key": "q8_theme",
        "scale": "behavioral",
        "left_key": "q8_left",
        "right_key": "q8_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 9,
        "theme_key": "q9_theme",
        "scale": "behavioral",
        "left_key": "q9_left",
        "right_key": "q9_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 10,
        "theme_key": "q10_theme",
        "scale": "behavioral",
        "left_key": "q10_left",
        "right_key": "q10_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 11,
        "theme_key": "q11_theme",
        "scale": "behavioral",
        "left_key": "q11_left",
        "right_key": "q11_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 12,
        "theme_key": "q12_theme",
        "scale": "behavioral",
        "left_key": "q12_left",
        "right_key": "q12_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 13,
        "theme_key": "q13_theme",
        "scale": "behavioral",
        "left_key": "q13_left",
        "right_key": "q13_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 14,
        "theme_key": "q14_theme",
        "scale": "behavioral",
        "left_key": "q14_left",
        "right_key": "q14_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 15,
        "theme_key": "q15_theme",
        "scale": "behavioral",
        "left_key": "q15_left",
        "right_key": "q15_right",
        "left_score": 1,
        "right_score": 0,
    },
    {
        "id": 16,
        "theme_key": "q16_theme",
        "scale": "behavioral",
        "left_key": "q16_left",
        "right_key": "q16_right",
        "left_score": 1,
        "right_score": 0,
    },
]

BEHAVIORAL_QUESTION_IDS = [q["id"] for q in QUESTIONS if q["scale"] == "behavioral"]
ECONOMIC_QUESTION_IDS = [q["id"] for q in QUESTIONS if q["scale"] == "economic"]

BEHAVIORAL_THRESHOLDS = {
    "left": (8, 10),
    "center_left": (6, 7),
    "center": (5, 5),
    "center_right": (3, 4),
    "right": (0, 2),
}

ECONOMIC_THRESHOLDS = {
    "left": (5, 6),
    "center_left": (4, 4),
    "center": (3, 3),
    "center_right": (2, 2),
    "right": (0, 1),
}

GENERAL_THRESHOLDS = {
    "left": (9, 12),
    "center_left": (7, 8),
    "center": (6, 6),
    "center_right": (4, 5),
    "right": (0, 3),
}

CLASSIFICATION_KEYS = ["left", "center_left", "center", "center_right", "right"]

SCALE_LABELS_KEYS = {
    "left": "classification_left",
    "center_left": "classification_center_left",
    "center": "classification_center",
    "center_right": "classification_center_right",
    "right": "classification_right",
}

EXPLANATION_KEYS = {
    "behavioral": {
        "left": "explanation_behavioral_left",
        "center_left": "explanation_behavioral_center_left",
        "center": "explanation_behavioral_center",
        "center_right": "explanation_behavioral_center_right",
        "right": "explanation_behavioral_right",
    },
    "economic": {
        "left": "explanation_economic_left",
        "center_left": "explanation_economic_center_left",
        "center": "explanation_economic_center",
        "center_right": "explanation_economic_center_right",
        "right": "explanation_economic_right",
    },
    "general": {
        "left": "explanation_general_left",
        "center_left": "explanation_general_center_left",
        "center": "explanation_general_center",
        "center_right": "explanation_general_center_right",
        "right": "explanation_general_right",
    },
}

MAX_BEHAVIORAL = 10
MAX_ECONOMIC = 6
MAX_GENERAL = 12