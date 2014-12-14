from xmlrpclib import ServerProxy
# https://docs.python.org/2/library/xmlrpclib.html

proxy = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

## list methods
#>>> proxy.system.listMethods()
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

## get phone signature
#>>> proxy.system.methodSignature('phone')
#[['string', 'string']]

# test phone method
#>>> proxy.phone('teste')
#'He is not the evil'

print proxy.phone('Bert')
