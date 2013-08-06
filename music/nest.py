import sys
from subprocess import *
import os
import urllib2
import simplejson
from pyechonest import config
from pyechonest import song

config.ECHO_NEST_API_KEY = "CPS7RW8QAUIULBBVJ"

def main():
  if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " ARTIST TITLE"
    return

  songs = song.search(artist = sys.argv[1], title = sys.argv[2], buckets = ["audio_summary"])
  data = {}

  print "Matching songs:", len(songs)

  for s in songs:
    print s
    data = Popen("curl \"" + s.audio_summary["analysis_url"] + "\"", shell=True, stdout=PIPE).stdout
    print simplejson.load(data)["bars"]
    break

if __name__ == "__main__":
  main()
