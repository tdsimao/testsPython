from PIL import Image
import zipfile, urllib, re
url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
fileName = 'data/oxygen.png'
file = urllib.urlretrieve(url,fileName)
im = Image.open(fileName)
line = im.size[1]/2
s = ''
for x in range(0,im.size[0],7):
    s = s + chr(im.getpixel((x,line))[0])
#print s
l = re.findall('[0-9]+',s)
s = ''
for n in l:
    s = s + chr(int(n))
print s

