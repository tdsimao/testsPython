import string
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet = string.lowercase


#first solution
for c in text:
    if c in alphabet:
        print alphabet[(alphabet.index(c)+2)%23],
    else:
        print c,
print 

#second solution
def decrypt(text):
    table = string.maketrans(alphabet, alphabet[2:]+alphabet[:2])
    return string.translate(text,table)
print decrypt(text)
print decrypt('http://www.pythonchallenge.com/pc/def/map.html') 
