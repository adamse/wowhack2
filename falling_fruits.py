# vim: set fileencoding=utf8
import sys, os, pygame, random
from pygame.locals import *


image_dir = "bilder"
# The size of the screen
size = width, height = 660, 700
# The screen is global, so the Fruit-class can get access to it
screen = pygame.display.set_mode(size)

# The x coordinates for the different fruits
lemon_x = 110
apple_x = 330
banana_x = 550

class Fruit:
    def __init__(self, fruit, speed=0.5):
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
        self.banana_image, self.banana_rect = self.createFruitContour("banana", banana_x)
        self.apple_image, self.apple_rect = self.createFruitContour("apple", apple_x)
        self.lemon_image, self.lemon_rect = self.createFruitContour("lemon", lemon_x)

    def createFruitContour(self, fruit_name, x):
        image = pygame.image.load(os.path.join('bilder', fruit_name + "_linjer.png")).convert()
        image = pygame.transform.scale(image, (128, 128))

        image.set_colorkey((120, 120, 0))

        rect = image.get_rect()

        rect.midtop = (x, height - 144)

        screen.blit(image, rect)

        return (image, rect)

    def blit(self):
        screen.blit(self.banana_image, self.banana_rect)
        screen.blit(self.apple_image, self.apple_rect)
        screen.blit(self.lemon_image, self.lemon_rect)


def generateRandomFruit():
    fruits = ["banana", "apple", "lemon"]
    index = random.randint(0, 2)
    fruit_type = fruits[index]
    fruit = Fruit(fruit_type)
    return fruit

def main():
    black = 0, 0, 0

    SCORE = 0

    clock = pygame.time.Clock()

    fruit_contours = FruitContours()

    fruits = {
      "lemon": [],
      "apple": [],
      "banana": []
    }

    pygame.init()

    # A dictionary for which buttons that will generate what fruit
    fruitdir = {K_UP: "apple", K_LEFT: "lemon", K_RIGHT: "banana"}

    while 1:
        screen.fill(black)

        delta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                if button == K_ESCAPE: return
                elif button in (K_UP,K_LEFT,K_RIGHT):
                  for l in (fruits["lemon"], fruits["banana"], fruits["apple"]):
                    for f in l:
                      if f.fruit == fruitdir[button] and f.rect.bottom > (height - 150):
                        print 'Well done, you saved the ' + f.fruit + '!'
                        SCORE += 1
                        print SCORE
                        break

        # Move and blit all the fruits on the screen
        for l in (fruits["lemon"], fruits["banana"], fruits["apple"]):
          for index, fruit in enumerate(l):
            if fruit.move(delta):
              fruit.blit()
            else:
              fruits[fruit.fruit].pop(index)

        # Generate random fruits
        if random.randint(0, 100) > 97:
            new_fruit = generateRandomFruit()

            fruits[new_fruit.fruit].append(new_fruit)


        # Draw the fruit contours
        fruit_contours.blit()

        pygame.display.flip()

if __name__ == '__main__': main()
