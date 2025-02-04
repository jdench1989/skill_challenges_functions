from lib.count_words import count_words
import pytest

def test_when_given_empty_string_returns_0():
    expected = 0
    actual = count_words("")
    assert actual == expected

def test_when_given_string_of_5_words_returns_5():
    expected = 5
    actual = count_words("A string of five words")
    assert actual == expected

def test_return_TypeError_when_input_not_string():
    expected = "Input must be a string"
    with pytest.raises(TypeError) as e:
        count_words(1234)
    actual = str(e.value)
    assert actual == expected