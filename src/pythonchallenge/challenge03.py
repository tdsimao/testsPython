import re
from lib.misc import *
retrieve_file('http://www.pythonchallenge.com/pc/def/equality.html','data/challenge03.txt')
f = open('data/challenge03.txt')
text = f.read()
pattern = ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))
print pattern
