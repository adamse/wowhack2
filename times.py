import simplejson, pygame

falling_distance = 400 # this is just a guess: we'll have to check the actual falling distance for fruits in pixels
default_speed = 0.4

class Times:
  def __init__(self, json="daft_punk.json"):
    with open(json) as f:
      self.data = simplejson.load(f)

  def bars(self):
    return [t["start"] for t in self.data["bars"]]

  def beats(self):
    return [t["start"] for t in self.data["beats"]]

  def sections(self):
    return [t["start"] for t in self.data["sections"]]

def main():
    times = Times()
    beats = times.beats()
    sections = times.sections()
    bars = times.bars()

    clock = pygame.time.Clock()

    clock.tick()

    song_time = 0

    last_beat_time = 0
    extra_beat_time = 1000
    extra_beat = False

    falling_time = falling_distance / (default_speed * 1000)

    while 1:
        song_time += (clock.tick() / float(1000))

        # Check if the song is finished
        if len(beats) > 0:
            # If there's an extra beat, do something before it
            if (extra_beat and song_time + falling_time >= extra_beat_time):
                print("Extra beat!")
                print("Time now + falling time: " + str(song_time + falling_time))
                print("Extra beat time: " + str(extra_beat_time))
                print("")

                extra_beat = False

            # If not, do something before every beat
            if (song_time + falling_time >= beats[0]):
                time_between_beats = beats[0] - last_beat_time
                extra_beat_time = beats[0] + (time_between_beats / 2)
                
                print("Dance before the beat!")
                print("Time now + falling time: " + str(song_time + falling_time))
                print("Beat time: " + str(beats[0]))
                print("")

                extra_beat = not extra_beat

                last_beat_time = beats[0]
                beats.pop(0)

if __name__ == '__main__' : main()


