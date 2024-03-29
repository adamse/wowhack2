# vim: set fileencoding=utf8
import sys, os, pygame, random, times
from pygame.locals import *
from background import Background

image_dir = "bilder"
# The size of the screen
size = width, height = 660, 700
# The screen is global, so the Fruit-class can get access to it
screen = pygame.display.set_mode(size)

# The x coordinates for the different fruits
lemon_x = 110
apple_x = 330
banana_x = 550

# Magic glow time
magic_glow_time = 10

# Default fruit falling speed
fruit_falling_speed = 0.5
# Distance for fruit to fall until it's in catch area
fruit_falling_distance = 700

class Fruit:
    def __init__(self, fruit, speed=fruit_falling_speed):
        # Load the image
        self.image = pygame.image.load(os.path.join('bilder', fruit + ".png")).convert()

        self.fruit = fruit

        # Set white to the transparent color
        self.image.set_colorkey((120, 120, 0))

        # Resize the image
        self.image = pygame.transform.scale(self.image, (128, 128))

        self.rect = self.image.get_rect()

        # Determine the x coordinate of the fruit according to which fruit it is
        if fruit == "lemon":
            self.x = lemon_x
        elif fruit == "banana":
            self.x = banana_x
        elif fruit == "apple":
            self.x = apple_x

        # Make the fruit appear outside the screen at the top
        self.rect.midtop = (self.x, -100)

        # The speed of which the fruit will fall
        self.speed = speed

        # Is the fruit hit?
        self.hit = False

    # Blits the fruit to the screen
    def blit(self):
        screen.blit(self.image, self.rect)

    # Moves the fruit according to the set speed and the time delta
    # (this is so the fruit moves to actual time passed, which could differ for every iteration of the game loop)
    # returns True if were still on screen
    def move(self, delta):
        self.rect = self.rect.move((0, self.speed * delta))
        return (self.rect.y <= height)

class FruitContours:
  def __init__(self):
    self.banana, self.banana_glow, self.banana_rect = self.createFruitContour("banana", banana_x)
    self.apple, self.apple_glow, self.apple_rect = self.createFruitContour("apple", apple_x)
    self.lemon, self.lemon_glow, self.lemon_rect = self.createFruitContour("lemon", lemon_x)

    self.bglow = 0
    self.aglow = 0
    self.lglow = 0

  def createFruitContour(self, fruit_name, x):
    image = pygame.image.load(os.path.join('bilder', fruit_name + "_linjer.png")).convert()
    glow = pygame.image.load(os.path.join("bilder", fruit_name + "_linjer_glow.png")).convert()
    image = pygame.transform.scale(image, (128, 128))
    glow = pygame.transform.scale(glow, (128, 128))

    image.set_colorkey((120, 120, 0))
    glow.set_colorkey((120, 120, 0))

    rect = image.get_rect()

    rect.midtop = (x, height - 150) # magic number

    screen.blit(image, rect)

    return (image, glow, rect)

  def blit(self):
    screen.blit(self.banana if self.bglow < 1 else self.banana_glow, self.banana_rect)
    screen.blit(self.apple if self.aglow < 1 else self.apple_glow, self.apple_rect)
    screen.blit(self.lemon if self.lglow < 1 else self.lemon_glow, self.lemon_rect)

  def glow_banana(self):
    self.bglow = magic_glow_time

  def glow_apple(self):
    self.aglow = magic_glow_time

  def glow_lemon(self):
    self.lglow = magic_glow_time

  def unglow(self):
      self.bglow -= 1
      self.lglow -= 1
      self.aglow -= 1

  def glow(self, fruit):
    if fruit == "banana":
      self.glow_banana()
    elif fruit == "lemon":
      self.glow_lemon()
    elif fruit == "apple":
      self.glow_apple()

def generateRandomFruit():
  return Fruit(random.choice(["banana", "apple", "lemon"]))

# This isn't used in the final game
def shouldGenerateFruit():
  return random.randint(1,100) > 97

def main():
  black = 0, 0, 0

  SCORE = 0

  clock = pygame.time.Clock()
  pygame.init()

  start = pygame.image.load("start.png").convert()
  start = pygame.transform.scale(start, (width, width))
  screen.blit(start, (0, 0))
  pygame.display.flip()

  n = True
  while n:
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        n = False
        break

  fruit_contours = FruitContours()
  back = Background(screen, width, height)
  fruits = []

  beat_timer = times.BeatTimer(fruit_falling_speed, fruit_falling_distance)


  # A dictionary for which buttons that will generate what fruit
  fruitdir = {K_UP: "apple", K_LEFT: "lemon", K_RIGHT: "banana"}

  # PLay that music you!
  pygame.mixer.init()
  pygame.mixer.Sound("harder.ogg").play()

  while 1:
    screen.fill(black)

    fruit_contours.unglow()

    delta = clock.tick(30)

    for event in pygame.event.get():
      if event.type == QUIT: return
      elif event.type == KEYDOWN:
        button = event.key
        if button == K_ESCAPE:
          print "You win:", SCORE, "points!", "HIGHSCORE!"
          return
        elif button in (K_UP,K_LEFT,K_RIGHT):
          for f in fruits:
            if f.hit == False and f.fruit == fruitdir[button] and f.rect.bottom > (height - 150):
              SCORE += 1
              fruit_contours.glow(f.fruit)
              f.hit = True
              break
            # Lose points if you're cheating
            elif f == fruits[-1]: SCORE -= 1

    back.blit()

    # Move and blit all the fruits on the screen
    for index, fruit in enumerate(fruits):
      if fruit.move(delta):
        fruit.blit()
      else:
        if not fruit.hit: SCORE -= 1
        fruits.pop(index)

    # Generate random fruits
    if beat_timer.get_beat(delta):
      new_fruit = generateRandomFruit()

      fruits.append(new_fruit)

    # Draw the fruit contours
    fruit_contours.blit()

    pygame.display.flip()
    pygame.display.set_caption("Score: " + str(SCORE))

if __name__ == '__main__': main()
