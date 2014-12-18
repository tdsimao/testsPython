import urllib,re,urllib2, cookielib, bz2
from xmlrpclib import ServerProxy
number = '12345'


s = ''

print 'start'
while True:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+number
    text = opener.open(url).read()
    for c in cj:
        s = s + c.value
    print text
    try:
        number = re.findall('[0-9]+',text)[-1]
    except:
        print s
        break


print s
dec = urllib.unquote_plus(s) 
s = bz2.decompress(dec)
print s

proxy = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')


print proxy.phone('Leopold')
#violin
#http://www.pythonchallenge.com/pc/return/violin.html
#no! i mean yes! but ../stuff/violin.php.

#http://www.pythonchallenge.com/pc/stuff/violin.php


