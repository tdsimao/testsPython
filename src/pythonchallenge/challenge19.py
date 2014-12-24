from lib.misc import retrieve_file
from PIL import Image
import gzip,difflib
import base64

from email.parser import Parser
#import email


fileName = 'data/bin.html'
retrieve_file('http://www.pythonchallenge.com/pc/hex/bin.html',fileName)

#file = open(fileName)


text = open(fileName).readlines()
mail = ''.join(text[14:1987])
att = ''.join(text[28:1986])

headers = Parser().parsestr(mail)

#print headers['Subject']
#print 'Content-type:',headers['Content-type']

text = base64.b64decode(att)

f = open('data/indian.wav','wb')
f.write(text)
f.close()

#headers = email.parser.Parser().parse(file)


