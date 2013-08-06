import urllib2
import simplejson

k = "1ZZLRKF6Z9IN6OBUI"

req =urllib2.Request(
"http://developer.echonest.com/api/v4/song/profile?api_key="
    + k + "&id=spotify:track:0MYTcPXAAmeKBUpBgtAV0J")
opener = urllib2.build_opener()
f = opener.open(req)
suicide = simplejson.load(f)

print(suicide)
