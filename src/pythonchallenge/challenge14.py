from lib.misc import *
from PIL import Image

fileName = 'data/wire.png'
retrieve_file('http://www.pythonchallenge.com/pc/return/wire.png',fileName)
im = Image.open(fileName)
size = im.size

im_out = Image.new('RGB',(100,100))
 
i = 0
try:
    for a in range(50):
        x = a
        y = a
        indices = range(a,100-a)
        #print indices
        print len(indices)
        print indices, indices[1::], indices[-2::-1], indices[-2:0:-1]
        
        for x in indices:
            im_out.putpixel((x,y),im.getpixel((i,0)))
            i = i+1
        for y in indices[1::]:
            im_out.putpixel((x,y),im.getpixel((i,0)))
            i = i + 1
        for x in indices[-2::-1]:
            im_out.putpixel((x,y),im.getpixel((i,0)))
            i = i + 1
        for y in indices[-2:0:-1]:
            im_out.putpixel((x,y),im.getpixel((i,0)))
            i = i + 1
except:
    pass
im_out.show()

