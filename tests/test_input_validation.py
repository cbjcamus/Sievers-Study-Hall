"""Tests for input validation."""

import pytest
from flask import Flask
from webapp.routes.exercises import validate_and_sanitize_answer, MAX_ANSWER_LENGTH


def test_validate_answer_accepts_valid_input():
    """Should accept valid text input."""
    result = validate_and_sanitize_answer("correct answer")
    assert result == "correct answer"


def test_validate_answer_strips_whitespace():
    """Should strip leading and trailing whitespace."""
    result = validate_and_sanitize_answer("  answer  ")
    assert result == "answer"


def test_validate_answer_removes_null_bytes():
    """Should remove null bytes from input."""
    result = validate_and_sanitize_answer("test\x00input")
    assert "\x00" not in result
    assert result == "testinput"


def test_validate_answer_rejects_non_string():
    """Should reject non-string input."""
    app = Flask(__name__)
    with app.app_context():
        with pytest.raises(Exception):
            validate_and_sanitize_answer(12345)


def test_validate_answer_rejects_oversized_input():
    """Should reject input exceeding maximum length."""
    app = Flask(__name__)
    with app.app_context():
        oversized = "a" * (MAX_ANSWER_LENGTH + 1)
        with pytest.raises(Exception):
            validate_and_sanitize_answer(oversized)


def test_validate_answer_accepts_max_length():
    """Should accept input at maximum length."""
    result = validate_and_sanitize_answer("a" * MAX_ANSWER_LENGTH)
    assert len(result) == MAX_ANSWER_LENGTH


def test_validate_answer_accepts_unicode():
    """Should accept unicode characters."""
    result = validate_and_sanitize_answer("Größe")
    assert result == "Größe"


def test_max_answer_length_constant():
    """MAX_ANSWER_LENGTH should be a reasonable value."""
    assert MAX_ANSWER_LENGTH == 10000
