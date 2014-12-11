import os.path

from PIL import Image
import zipfile, urllib, re
fileName = 'data/evil2.gfx'
if not os.path.isfile(fileName):
#if True:
    url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
    file = urllib.urlretrieve(url,fileName)

f = open(fileName).read()

im1 = open('data/evil1.jpg','w')
im2 = open('data/evil2.jpg','w')
im3 = open('data/evil3.jpg','w')
im4 = open('data/evil4.jpg','w')
im5 = open('data/evil5.jpg','w')

for b in range(0,len(f),5):
    im1.write(f[b])
    im2.write(f[b+1])
    im3.write(f[b+2])
    im4.write(f[b+3])
    im5.write(f[b+4])

im1.close()
im2.close()
im3.close()
im4.close()
im5.close()


