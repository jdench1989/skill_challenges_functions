# sentence_checker Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def sentence_checker(text):
    """Checks the input text to ensure it is formatted correctly as a sentence i.e. starts with a capital letter and ends with suitable punctuation.

    Parameters: (list all parameters and their types)
        text: a string containing multiple words

    Returns: (state the return value and its type)
        Boolean

    Side effects: (state any side effects)
        None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string that is formatted correctly
Return True
"""
sentence_checker("This is a correct sentence.") => True
sentence_checker("Another correct sentence!") => True
sentence_checker("What about this one?") => True

"""
Given a string that is not formatted correctly
Returns False
"""
sentence_checker("an incorrect sentence") => False
sentence_checker("Another incorrect sentence") => False
sentence_checker("and this one!") => False

"""
Given a text of only one word
Returns True if formatted correctly and False if not
"""
sentence_checker("Hi!") => True
sentence_checker("hi") => False
sentence_checker("Hi") => False
sentence_checker("hi!") => False

"""
Given an empty string
Returns an error
"""
sentence_checker("") => Error: Input text cannot be empty

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
