import os.path

from PIL import Image
from StringIO import StringIO
import zipfile, urllib, re
fileName = 'data/evil2.gfx'
if not os.path.isfile(fileName):
#if True:
    url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    file = urllib.urlretrieve(url,fileName)


s = open(fileName,'rb').read()

im1 = open('data/evil1.jpg','w')
im2 = open('data/evil2.jpg','w')
im3 = open('data/evil3.jpg','w')
im4 = open('data/evil4.jpg','w')
im5 = open('data/evil5.jpg','w')

for b in range(0,len(s),5):
    im1.write(s[b])
    im2.write(s[b+1])
    im3.write(s[b+2])
    im4.write(s[b+3])
    im5.write(s[b+4])

im1.close()
im2.close()
im3.close()
im4.close()
im5.close()

for i in range(5):	
    data = s[i::5]
    im = Image.open(StringIO(data))
    f = open('data/evil_%d.%s' % (i,im.format.lower()),'wb')
    f.write(data)
    f.close()
