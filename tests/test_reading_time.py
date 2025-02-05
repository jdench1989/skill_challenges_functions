from lib.reading_time import *
import pytest

"""
Given a string of 200 words in length
It returns 1.0
"""
def test_given_200_words_returns_1():
    text = " ".join(["word" for i in range(0, 200)])
    result = reading_time(text)
    assert result == 1.0

"""
Given a string of a length that is not a multiple of 200
Returns the number of minutes to read
"""
def test_given_100_words_returns_half():
    text = " ".join(["word" for i in range(0, 100)])
    result = reading_time(text)
    assert result == 0.5

"""
Given an empty string
it returns an error
"""
def test_given_empty_string_returns_error():
    text = ""
    with pytest.raises(Exception) as e:
        reading_time(text)
    result = str(e.value)
    assert result == "Error: Text cannot be empty"