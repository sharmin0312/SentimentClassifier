
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(a):
    b=""
    for i in a:
        if i in a and i not in punctuation_chars:
            b+=i
    return b
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(a):
    li=a.split()
    xi=[]
    for i in li:
        x=strip_punctuation(i)
        xi.append(x.lower())
    ct=0
    print("Next Line")
    for i in xi:
        if i in xi and i in negative_words:
            print(i)
            ct=ct+1
    return ct

