import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from event_analyzer import analyze_event
from fact_checker import fact_check
from topic_generator import generate_starters, save_feedback, get_history

# ==================== EVENT ANALYZER TESTS ====================
class TestEventAnalyzer:
    def test_analyze_event_returns_dict(self):
        result = analyze_event("AI and Machine Learning Conference 2024")
        assert isinstance(result, dict)

    def test_analyze_event_has_required_keys(self):
        result = analyze_event("Blockchain in Healthcare Summit")
        assert "themes" in result
        assert "industry" in result
        assert "tone" in result

    def test_analyze_event_themes_is_list(self):
        result = analyze_event("Climate Change and Sustainability Forum")
        assert isinstance(result["themes"], list)

    def test_analyze_event_not_empty(self):
        result = analyze_event("Tech Startup Networking Event")
        assert len(result["themes"]) > 0
        assert result["industry"] != ""
        assert result["tone"] != ""

# ==================== FACT CHECKER TESTS ====================
class TestFactChecker:
    def test_fact_check_returns_dict(self):
        result = fact_check("artificial intelligence")
        assert isinstance(result, dict)

    def test_fact_check_has_required_keys(self):
        result = fact_check("machine learning")
        assert "found" in result
        assert "query" in result
        assert "summary" in result

    def test_fact_check_known_topic(self):
        result = fact_check("Python programming language")
        assert result["found"] == True
        assert result["summary"] != ""

    def test_fact_check_source_url(self):
        result = fact_check("blockchain technology")
        if result["found"]:
            assert result["source"] is not None
            assert "wikipedia" in result["source"]

# ==================== TOPIC GENERATOR TESTS ====================
class TestTopicGenerator:
    def test_generate_starters_returns_dict(self):
        result = generate_starters(
            "AI Conference",
            "machine learning",
            ["AI", "technology"]
        )
        assert isinstance(result, dict)

    def test_generate_starters_has_starters_key(self):
        result = generate_starters(
            "Tech Networking Event",
            "startups, innovation",
            ["technology", "entrepreneurship"]
        )
        assert "starters" in result
        assert "entry_id" in result

    def test_generate_starters_count(self):
        result = generate_starters(
            "Healthcare Innovation Summit",
            "digital health",
            ["healthcare", "AI"]
        )
        assert len(result["starters"]) == 3

    def test_generate_starters_not_empty(self):
        result = generate_starters(
            "Climate Tech Forum",
            "sustainability",
            ["climate", "technology"]
        )
        for starter in result["starters"]:
            assert len(starter) > 0

# ==================== HISTORY & FEEDBACK TESTS ====================
class TestHistoryAndFeedback:
    def test_get_history_returns_list(self):
        result = get_history()
        assert isinstance(result, list)

    def test_save_feedback_success(self):
        result = save_feedback(1, 1, "thumbs_up")
        assert result["status"] == "success"

    def test_save_feedback_thumbs_down(self):
        result = save_feedback(1, 2, "thumbs_down")
        assert result["status"] == "success"