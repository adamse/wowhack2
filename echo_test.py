import urllib2
import simplejson

req = urllib2.Request("http://developer.echonest.com/api/v4/artist/search?api_key=1ZZLRKF6Z9IN6OBUI&name=suicide")
opener = urllib2.build_opener()
f = opener.open(req)
suicide = simplejson.load(f)

print(suicide)
