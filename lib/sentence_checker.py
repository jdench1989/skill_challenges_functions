def sentence_checker(text):
    if text == "":
        raise Exception("Error: Input text cannot be empty")
    else:
        if text[0].isupper() and text[-1] in "!?.":
            return True
        else:
            return False