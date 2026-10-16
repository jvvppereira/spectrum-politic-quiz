import pytest
from src.core.scoring import (
    calculate_behavioral_score,
    calculate_economic_score,
    calculate_general_score,
    classify_score,
    calculate_all_scores,
)
from src.core.questions import BEHAVIORAL_QUESTION_IDS, ECONOMIC_QUESTION_IDS


class TestBehavioralScoring:
    def test_all_left_answers_max_score(self):
        answers = {q: 1 for q in BEHAVIORAL_QUESTION_IDS}
        assert calculate_behavioral_score(answers) == 10
    
    def test_all_right_answers_min_score(self):
        answers = {q: 0 for q in BEHAVIORAL_QUESTION_IDS}
        assert calculate_behavioral_score(answers) == 0
    
    def test_mixed_answers(self):
        answers = {
            7: 1, 8: 0, 9: 1, 10: 0,
            11: 1, 12: 0, 13: 1, 14: 0,
            15: 1, 16: 0
        }
        assert calculate_behavioral_score(answers) == 5
    
    def test_partial_answers(self):
        answers = {7: 1, 8: 1, 9: 1}
        assert calculate_behavioral_score(answers) == 3
    
    def test_missing_questions_treated_as_zero(self):
        answers = {7: 1}
        assert calculate_behavioral_score(answers) == 1


class TestEconomicScoring:
    def test_all_left_answers_max_score(self):
        answers = {q: 1 for q in ECONOMIC_QUESTION_IDS}
        assert calculate_economic_score(answers) == 6
    
    def test_all_right_answers_min_score(self):
        answers = {q: 0 for q in ECONOMIC_QUESTION_IDS}
        assert calculate_economic_score(answers) == 0
    
    def test_mixed_answers(self):
        answers = {1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0}
        assert calculate_economic_score(answers) == 3
    
    def test_partial_answers(self):
        answers = {1: 1, 2: 1}
        assert calculate_economic_score(answers) == 2


class TestGeneralScoring:
    def test_max_scores(self):
        # behavioral=10 -> 6.0 normalized, economic=6 -> total=12
        assert calculate_general_score(10, 6) == 12
    
    def test_min_scores(self):
        assert calculate_general_score(0, 0) == 0
    
    def test_mid_scores(self):
        # behavioral=5 -> 3.0, economic=3 -> total=6
        assert calculate_general_score(5, 3) == 6
    
    def test_rounding(self):
        # behavioral=7 -> 4.2, economic=2 -> 6.2 -> 6
        assert calculate_general_score(7, 2) == 6
        # behavioral=8 -> 4.8, economic=2 -> 6.8 -> 7
        assert calculate_general_score(8, 2) == 7
    
    def test_weighted_50_50(self):
        # Behavioral contributes 6/12 = 50%, Economic contributes 6/12 = 50%
        # behavioral=10 (max) + economic=0 = 6
        # behavioral=0 + economic=6 (max) = 6
        assert calculate_general_score(10, 0) == 6
        assert calculate_general_score(0, 6) == 6


class TestClassification:
    @pytest.mark.parametrize("score,expected", [
        (10, "left"), (9, "left"), (8, "left"),
        (7, "center_left"), (6, "center_left"),
        (5, "center"),
        (4, "center_right"), (3, "center_right"),
        (2, "right"), (1, "right"), (0, "right"),
    ])
    def test_behavioral_thresholds(self, score, expected):
        assert classify_score(score, "behavioral") == expected
    
    @pytest.mark.parametrize("score,expected", [
        (6, "left"), (5, "left"),
        (4, "center_left"),
        (3, "center"),
        (2, "center_right"),
        (1, "right"), (0, "right"),
    ])
    def test_economic_thresholds(self, score, expected):
        assert classify_score(score, "economic") == expected
    
    @pytest.mark.parametrize("score,expected", [
        (12, "left"), (11, "left"), (10, "left"), (9, "left"),
        (8, "center_left"), (7, "center_left"),
        (6, "center"),
        (5, "center_right"), (4, "center_right"),
        (3, "right"), (2, "right"), (1, "right"), (0, "right"),
    ])
    def test_general_thresholds(self, score, expected):
        assert classify_score(score, "general") == expected
    
    def test_invalid_scale_type(self):
        with pytest.raises(ValueError):
            classify_score(5, "invalid")


class TestCalculateAllScores:
    def test_all_left_answers(self):
        answers = {q: 1 for q in range(1, 17)}
        results = calculate_all_scores(answers)
        
        assert results["behavioral_score"] == 10
        assert results["behavioral_classification"] == "left"
        assert results["economic_score"] == 6
        assert results["economic_classification"] == "left"
        assert results["general_score"] == 12
        assert results["general_classification"] == "left"
    
    def test_all_right_answers(self):
        answers = {q: 0 for q in range(1, 17)}
        results = calculate_all_scores(answers)
        
        assert results["behavioral_score"] == 0
        assert results["behavioral_classification"] == "right"
        assert results["economic_score"] == 0
        assert results["economic_classification"] == "right"
        assert results["general_score"] == 0
        assert results["general_classification"] == "right"
    
    def test_center_answers(self):
        # 5 behavioral left, 3 economic left
        answers = {}
        for i, qid in enumerate(BEHAVIORAL_QUESTION_IDS):
            answers[qid] = 1 if i < 5 else 0
        for i, qid in enumerate(ECONOMIC_QUESTION_IDS):
            answers[qid] = 1 if i < 3 else 0
        
        results = calculate_all_scores(answers)
        
        assert results["behavioral_score"] == 5
        assert results["behavioral_classification"] == "center"
        assert results["economic_score"] == 3
        assert results["economic_classification"] == "center"
        # behavioral=5 -> 3.0, economic=3 -> 6.0
        assert results["general_score"] == 6
        assert results["general_classification"] == "center"
    
    def test_includes_max_values(self):
        answers = {q: 0 for q in range(1, 17)}
        results = calculate_all_scores(answers)
        
        assert results["behavioral_max"] == 10
        assert results["economic_max"] == 6
        assert results["general_max"] == 12