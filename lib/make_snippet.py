def make_snippet(string):
    words = string.split()
    if len(words) > 5:
        return_string = " ".join(words[:5]) + " ..."
        return return_string
    else:
        return string