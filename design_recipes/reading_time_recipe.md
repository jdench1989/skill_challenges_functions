# reading_time Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text):
    """
    Estimates reading time based on a speed of 200 wpm.

    Parameters:
        text: A string of words representing a piece of text. 

    Returns:
        An float representing an estimate of the number of minutes to read the text (two decimal places)

    Side-effects:
        None
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python


"""
Given a string of a multiple of 200 words in length
It returns the number of minutes to read that string as a float
"""
reading_time("string of 200 words") => 1

"""
Given a string of a length that is not a multiple of 200
Returns the number of minutes to read
"""
reading_time("string of 100 words") => 1


"""
Given an empty string
it returns an error
"""
reading_time("") => "Error: Text cannot be empty


```


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
