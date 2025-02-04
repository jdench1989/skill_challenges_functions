"""
Test-drive a function with the following design:

Design
A function called count_words that takes a string as an argument and returns the number of words in that string.
"""

def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = text.split()
    return len(words)