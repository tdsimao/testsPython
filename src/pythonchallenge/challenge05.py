import zipfile, re, pickle, urllib

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
file = urllib.urlopen(url)
data = pickle.load(file)

for line in data:
    s = ''
    for (c,n) in line:
        s = s + c*n
    print s

file.close()
