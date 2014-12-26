from lib.misc import retrieve_file
from PIL import Image
import gzip,difflib
import base64
import email
import mimetools

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

audiodata = base64.b64decode(att)

input = open('data/indian.dat','wb')
input.write(att)
input.close()

input = open('data/indian.dat','rb')
output = open('data/indian.wav','wb')

#print dir(email.mime.Audio)
#aux = email.mime.audio.MIMEAudio(audiodata)

#headers = email.parser.Parser().parse(file)

exit = ''
mimetools.decode(input, output, 'base64')
