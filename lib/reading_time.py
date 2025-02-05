def reading_time(text):
    if text == "":
        raise Exception("Error: Text cannot be empty")
    words = text.split()
    return len(words)/200