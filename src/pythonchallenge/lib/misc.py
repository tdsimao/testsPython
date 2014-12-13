import os.path
import urllib

def retrieve_file(url,path):
    """
       retrieve file from url if don't find it in path 
    """
    if not os.path.isfile(path):
        urllib.urlretrieve(url,path)
