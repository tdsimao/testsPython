from lib.misc import *
retrieve_file('http://www.pythonchallenge.com/pc/def/ocr.html','data/challenge02.txt')
f = open('data/challenge02.txt')
text = f.readlines()[38:1257]
d = {}
for l in text:
    for c in l:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1

for l in text:
    for c in l:
        if d[c] < 10:
            print c,
#print d
