
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(a):
    b=""
    for i in a:
        if i in a and i not in punctuation_chars:
            b+=i
    return b
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(a):
    li=a.split()
    xi=[]
    for i in li:
        x=strip_punctuation(i)
        xi.append(x.lower())
    ct=0
    print("Next Line")
    for i in xi:
        if i in xi and i in positive_words:
            print(i)
            ct=ct+1
    return ct
print(get_pos("what a truly Wonderful day it is today! #incredible"))          
