import urllib.request


""" The function bellow is for checking if there is internet 
 """
def checkConnection(host = "http://google.com"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
