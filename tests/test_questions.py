import pytest
from src.core.questions import (
    QUESTIONS,
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


class TestQuestionStructure:
    def test_question_count(self):
        assert len(QUESTIONS) == 16
    
    def test_scales_distribution(self):
        behavioral = [q for q in QUESTIONS if q["scale"] == "behavioral"]
        economic = [q for q in QUESTIONS if q["scale"] == "economic"]
        assert len(behavioral) == 10
        assert len(economic) == 6
    
    def test_behavioral_question_ids(self):
        assert BEHAVIORAL_QUESTION_IDS == [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    
    def test_economic_question_ids(self):
        assert ECONOMIC_QUESTION_IDS == [1, 2, 3, 4, 5, 6]
    
    def test_all_questions_have_required_keys(self):
        required_keys = ["id", "theme_key", "scale", "left_key", "right_key", "left_score", "right_score"]
        for q in QUESTIONS:
            for key in required_keys:
                assert key in q, f"Missing key {key} in question {q['id']}"
    
    def test_question_ids_sequential(self):
        ids = [q["id"] for q in QUESTIONS]
        assert ids == list(range(1, 17))
    
    def test_left_right_scores(self):
        for q in QUESTIONS:
            assert q["left_score"] == 1
            assert q["right_score"] == 0


class TestThresholds:
    def test_behavioral_thresholds_coverage(self):
        """All scores 0-10 should be covered exactly once."""
        covered = set()
        for cls, (min_s, max_s) in BEHAVIORAL_THRESHOLDS.items():
            for s in range(min_s, max_s + 1):
                assert s not in covered, f"Score {s} covered multiple times"
                covered.add(s)
        assert covered == set(range(0, 11))
    
    def test_economic_thresholds_coverage(self):
        """All scores 0-6 should be covered exactly once."""
        covered = set()
        for cls, (min_s, max_s) in ECONOMIC_THRESHOLDS.items():
            for s in range(min_s, max_s + 1):
                assert s not in covered
                covered.add(s)
        assert covered == set(range(0, 7))
    
    def test_general_thresholds_coverage(self):
        """All scores 0-12 should be covered exactly once."""
        covered = set()
        for cls, (min_s, max_s) in GENERAL_THRESHOLDS.items():
            for s in range(min_s, max_s + 1):
                assert s not in covered
                covered.add(s)
        assert covered == set(range(0, 13))
    
    def test_classification_keys_order(self):
        assert CLASSIFICATION_KEYS == ["left", "center_left", "center", "center_right", "right"]


class TestMaxValues:
    def test_max_behavioral(self):
        assert MAX_BEHAVIORAL == 10
    
    def test_max_economic(self):
        assert MAX_ECONOMIC == 6
    
    def test_max_general(self):
        assert MAX_GENERAL == 12