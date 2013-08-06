import simplejson, pygame

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

    while 1:
        song_time += (clock.tick() / float(1000))

        # will crash yeah
        if (song_time >= beats[0]):
            beats.pop(0)
            print("Dance to the section! " + str(beats[0]))

if __name__ == '__main__' : main()


