from lib.misc import *
import os.path

from PIL import Image
import zipfile, urllib, re
fileName = 'data/cave.jpg'
retrieve_file('http://www.pythonchallenge.com/pc/return/cave.jpg',fileName)
im = Image.open(fileName)
size = im.size
im_odd = Image.new('RGB',size)
im_even = Image.new('RGB',size)

i = 0
for x in range(size[0]):
    for y in range(size[1]):
        if ((x*y) % 2) == 0:
            im_even.putpixel((x,y),im.getpixel((x,y)))
        else:
            im_odd.putpixel((x,y),im.getpixel((x,y)))
        i = i+1
im_even.show()
im_odd.show()
im.show()

