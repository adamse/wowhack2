import simplejson, pygame

#     Times
# This class takes data from an Echo Nest JSON file (here hard-coded for a local daft punk song).
# It can return lists of the times of beats, bars and sections in the song, in seconds.
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


#     BeatTimer
# This class has a method, get_beat, that takes a time delta as a parameter
# It then tells if a beat should be played or not
# TODO: It should be able to say if the song is over or not
# TODO: It should be able to handle extra beats. 
# TODO: It should know different patterns for beats & extra beats, which it should be able 
#       to change up if a new section of the song starts.

class BeatTimer:

    def __init__(self, fruit_falling_speed, fruit_falling_distance):
        self.time_now = 0
        times = Times()
        self.beats = times.beats()

        # Calculate the time (in seconds) it takes for a fruit to arrive at the catch area after being generated
        self.falling_time = fruit_falling_distance / (fruit_falling_speed * 1000)

    # Returns true if 
    def get_beat(self, delta):
        self.time_now += (delta / float(1000))
        
        # Check if the song is still on
        if len(self.beats) > 0:
            # Check if there's an extra beat: if so, return true
            #TODO
            
            # Check if there's a normal beat: if so, return true
            if self.time_now + self.falling_time >= self.beats[0]:
                self.beats.pop(0)
                return True
        
        # If there were no new beat, return false
        return False

# This is a main method for testing the BeatTimer class
def main():

    falling_distance = 400
    default_speed = 0.4

    clock = pygame.time.Clock()
    clock.tick()

#    last_beat_time = 0
#    extra_beat_time = 1000

    beat_timer = BeatTimer(default_speed, falling_distance)

    while 1:
        if beat_timer.get_beat(clock.tick()):
            print("It's on!")

# Some old code, which can also handle extra beats
#
#        # Check if the song is finished
#        if len(beats) > 0:
#            # If there's an extra beat, do something before it
#            if (extra_beat and song_time + falling_time >= extra_beat_time):
#                print("Extra beat!")
#                print("Time now + falling time: " + str(song_time + falling_time))
#                print("Extra beat time: " + str(extra_beat_time))
#                print("")
#
#                extra_beat = False
#
#            # If not, do something before every beat
#            if (song_time + falling_time >= beats[0]):
#                time_between_beats = beats[0] - last_beat_time
#                extra_beat_time = beats[0] + (time_between_beats / 2)
#                
#                print("Dance before the beat!")
#                print("Time now + falling time: " + str(song_time + falling_time))
#                print("Beat time: " + str(beats[0]))
#                print("")
#
#                extra_beat = not extra_beat
#
#                last_beat_time = beats[0]
#                beats.pop(0)

if __name__ == '__main__' : main()


