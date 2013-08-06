import files
import play
from pyechonest import config
from pyechonest import song

config.ECHO_NEST_API_KEY = "CPS7RW8QAUIULBBVJ"

for k, v in files.files.iteritems():
  songs = song.search(artist = v["artist"], title = v["title"],
      buckets=["audio_summary"])
  print k
  print songs[0].audio_summary
