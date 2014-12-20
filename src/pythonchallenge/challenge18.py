from lib.misc import retrieve_file
from PIL import Image

fileName = 'data/baloons.jpg'
retrieve_file('http://www.pythonchallenge.com/pc/return/balloons.jpg',fileName)
im = Image.open(fileName)
(w,h) = im.size
im_out = Image.new(im.mode,(w/2,h))

bars = {}
for y in range(h):
    for x in range(w/2):
        p = [0]*3
        for i in range(3):
            p[i] = im.getpixel((x,y))[i] - im.getpixel((x+w/2,y))[i]
        #print im.getpixel((x,y)), im.getpixel((x+w/2,y)), tuple(p)
        #print p
        im_out.putpixel((x,y),tuple(p))
im_out.show()
#im.show()
#im_out.save('data/challenge-out_18.jpg')

# first clue
#http://www.pythonchallenge.com/pc/return/colors.html
#be more precise. +light : -light

