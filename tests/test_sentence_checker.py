from lib.sentence_checker import sentence_checker
import pytest

"""
Given a string that is formatted correctly
Return True
"""
def test_given_correct_formatted_string_returns_true():
    assert sentence_checker("This is a correct sentence.") == True
    assert sentence_checker("Another correct sentence!") == True
    assert sentence_checker("What about this one?") == True

"""
Given a string that is not formatted correctly
Returns False
"""
def test_given_incorrectly_formatted_string_returns_false():
    assert sentence_checker("an incorrect sentence") == False
    assert sentence_checker("Another incorrect sentence") == False
    assert sentence_checker("and this one!") == False

"""
Given a text of only one word
Returns True if formatted correctly and False if not
"""
def test_given_string_of_one_word_behaves_correctly():
    assert sentence_checker("Hi!") == True
    assert sentence_checker("hi") == False
    assert sentence_checker("Hi") == False
    assert sentence_checker("hi!") == False

"""
Given an empty string
Returns an error
"""
def test_given_empty_string_throws_exception():
    with pytest.raises(Exception) as e:
        sentence_checker("")
    error_message = str(e.value)
    assert error_message == "Error: Input text cannot be empty"