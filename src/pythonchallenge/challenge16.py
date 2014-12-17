from lib.misc import retrieve_file
from PIL import Image, ImageSequence


fileName = 'data/mozart.gif'
retrieve_file('http://www.pythonchallenge.com/pc/return/mozart.gif',fileName)
im = Image.open(fileName)
im_out = Image.new(im.mode,im.size)
im_out.palette = im.palette  # share colour table
size = im.size

#i = 0
bars = {}
for y in range(size[1]):
    for x in range(size[0]):
        if im.getpixel((x,y)) == 195 and im.getpixel((x+5,y)):
            bars[y] = x

for y in range(size[1]):
    for x in range(size[0]):
        new_x = (bars[y] + x) % size[0]
        im_out.putpixel((x,y),im.getpixel((new_x,y)))
    
im_out.show()
im_out.save('data/challenge_16_out.gif')
