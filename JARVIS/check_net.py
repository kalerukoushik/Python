import urllib.request as urllib2
import time
count = 1
if count == 1:
    try:
        urllib2.urlopen("http://google.com")
    except urllib2.URLError:
        print( "Network currently down." )
    else:
        print( "Up and running." )
        count = 0