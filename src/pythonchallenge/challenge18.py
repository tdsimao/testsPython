from lib.misc import retrieve_file
from PIL import Image

fileName = 'data/baloons.jpg'
retrieve_file('http://www.pythonchallenge.com/pc/return/balloons.jpg',fileName)
im = Image.open(fileName)
(w,h) = im.size

im1 = Image.new(im.mode,(w/2,h))
im2 = Image.new(im.mode,(w/2,h))

for y in range(h):
    for x in range(w/2):
         im1.putpixel((x,y),im.getpixel((x,y)))
         im2.putpixel((x,y),im.getpixel((x+w/2,y)))

#im.show()
#im_out.save('data/challenge-out_18.jpg')

# first clue
#http://www.pythonchallenge.com/pc/return/colors.html
#be more precise. +light : -light

#http://www.pythonchallenge.com/pc/return/brightness.html
#<!-- maybe consider deltas.gz -->
#http://www.pythonchallenge.com/pc/return/deltas.gz
deltas = 'data/deltas.gz'
retrieve_file('http://www.pythonchallenge.com/pc/return/deltas.gz',deltas)


