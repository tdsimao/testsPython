import urllib,re,urllib2, cookielib, bz2
from xmlrpclib import ServerProxy


number = '12345'
s = ''
while True:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+number
    text = opener.open(url).read()
    for c in cj:
        s = s + c.value
    #print text
    try:
        number = re.findall('[0-9]+',text)[-1]
    except:
        print s
        # BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
        break

#Replace %xx escapes in s by their single-character equivalent, also replace plus signs by spaces
s = urllib.unquote_plus(s) 

#Decompress data in one shot
s = bz2.decompress(s)

print s
#is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
proxy = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print proxy.phone('Leopold')
#555-VIOLIN

#violin
#http://www.pythonchallenge.com/pc/return/violin.html
#no! i mean yes! but ../stuff/violin.php.

#http://www.pythonchallenge.com/pc/stuff/violin.php
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
msg = "the flowers are on their way"
list(cj)[0].value = msg
opener.addheaders.append(('Cookie', 'value=%s' % msg))
print opener.open(url).read()	
#oh well, don't you dare to forget the balloons
