punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(a):
    b=""
    for i in a:
        if i in a and i not in punctuation_chars:
            b+=i
    return b
        