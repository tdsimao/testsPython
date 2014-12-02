import zipfile, urllib, re
url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
fileName = 'data/channel.zip'
originalFile = urllib.urlretrieve(url,fileName)
#zip = zipfile.ZipFile(originalFile,'r')
zip = zipfile.ZipFile(fileName,'r')

#zip = zipfile.ZipFile('data/channel.zip','r')
number = '90052'
#for name in zip.namelist():
while True:
    name = number+'.txt'
    file = zip.open(name,'r')
    print zip.getinfo(name).comment,
    text = file.read()
    try:
        number = re.findall('([0-9]+)',text)[0]
    except:
        break
    file.close()
zip.close()

