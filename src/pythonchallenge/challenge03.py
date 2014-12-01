
f = open('data/challenge03.txt')
text = f.readlines()
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
