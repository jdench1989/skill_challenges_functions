from lib.make_snippet import *

"""
When given an empty string, returns an empty string
"""
def test_when_given_empty_returns_empty():
    result = make_snippet("")
    assert result == ""

"""
When given a string of fewer than five words, returns the same string
"""
def test_when_given_fewer_than_5_words_returns_same_string():
    result = make_snippet("A short string")
    assert result == "A short string"

"""
When given a string of 5 words, returns the same string
"""
def test_when_given_5_words_returns_same_string():
    result = make_snippet("A string of five words")
    assert result == "A string of five words"

"""
When given a string of more than 5 words, returns the first five words with ... appended
"""
def test_when_given_more_thn_5_words_returns_first_five_with_ellipses():
    result = make_snippet("A string that is more than five words in length")
    assert result == "A string that is more ..."