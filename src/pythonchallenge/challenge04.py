import urllib,re
number = '12345'
#16044
number = '8022'
number = '63579'
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+number
    text = urllib.urlopen(url).read()
    print text
    number = re.findall('[0-9]+',text)[0]
