
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(a):
    b=""
    for i in a:
        if i in a and i not in punctuation_chars:
            b+=i
    return b

def get_pos(a):
    li=a.split()
    xi=[]
    for i in li:
        x=strip_punctuation(i)
        xi.append(x.lower())
    ct=0
    for i in xi:
        if i in xi and i in positive_words:
            ct=ct+1
    return ct


def get_neg(a):
    li=a.split()
    xi=[]
    for i in li:
        x=strip_punctuation(i)
        xi.append(x.lower())
    ct=0
    
    for i in xi:
        if i in xi and i in negative_words:
            ct=ct+1
    return ct

xi=[] 
with open("project_twitter_data.csv","r") as md:
    lines=md.readlines()
    
    for i in lines:
        li=[]
        st=i.split(",")
        tup=tuple(st)
        s,rt,rc=tup
        li.append(rt)
        li.append(rc.strip())
        li.append(str(get_pos(s)))
        li.append(str(get_neg(s)))
        net=get_pos(s)-get_neg(s)
        li.append(str(net))
        xi.append(li)
    del xi[0]  
with open("resulting_data.csv","w") as cd:
    head="Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score"
    cd.write(head)
    cd.write('\n')
    print(head)
    for i in xi:
        row = "{}, {}, {}, {}, {}".format(i[0],i[1],i[2],i[3],i[4])
        cd.write(row)
        cd.write('\n')
        print(row)
  