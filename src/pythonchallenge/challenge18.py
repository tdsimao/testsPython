from lib.misc import retrieve_file
from PIL import Image
import gzip,difflib


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

import ImageChops
im_out = ImageChops.difference(im1,im2)
#im_out.show('Teste')
#im_out.save('data/challenge-out_18.jpg')

# first clue
#http://www.pythonchallenge.com/pc/return/colors.html
#be more precise. +light : -light

#http://www.pythonchallenge.com/pc/return/brightness.html
#<!-- maybe consider deltas.gz -->
#http://www.pythonchallenge.com/pc/return/deltas.gz

deltas = 'data/deltas.gz'
retrieve_file('http://www.pythonchallenge.com/pc/return/deltas.gz',deltas)

lines = gzip.open(deltas,'rb').read().split('\n')

pairs = [ (l[:53], l[56:]) for l in lines]

left = [pair[0] for pair in pairs]
right = [pair[1] for pair in pairs]

diff = list(difflib.ndiff(left, right))

import codecs,re
for c in '-+ ':
    s = ''.join(filter(lambda l: l[0] == c , diff))
    # remove not hex characters and convert from hex 
    s = codecs.getdecoder('hex')(re.sub('[^0-9a-fA-F]', '', s))[0]
    fileName = 'data/challenge18_%c.png' % c
    f = open(fileName,'wb')
    f.write(s)
    f.close()
    im = Image.open(fileName)
    im.show()


