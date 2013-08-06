# vim: set fileencoding=utf8
import sys, os, pygame, random
from pygame.locals import *

# The size of the screen
size = width, height = 660, 700
# The screen is global, so the Fruit-class can get access to it
screen = pygame.display.set_mode(size)
# The default speed for the generated fruits
default_speed = 0.5
# The x coordinates for the different fruits
lemon_x = 110
apple_x = 330
banana_x = 550

class Fruit:
    def __init__(self, image_name, speed):
        # Load the image
        self.image = pygame.image.load(os.path.join('bilder', image_name + ".png")).convert()

        # Set white to the transparent color
        self.image.set_colorkey((120, 120, 0))

        # Resize the image
        self.image = pygame.transform.scale(self.image, (128, 128))

        self.rect = self.image.get_rect()

        # This is a bit ugly, but...
        # Determine the x coordinate of the fruit according to which fruit it is
        if image_name == "lemon":
            self.x = lemon_x
        elif image_name == "banana":
            self.x = banana_x
        elif image_name == "apple":
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
    fruit = Fruit(fruit_type, default_speed)
    return fruit

def main():
    black = 0, 0, 0

    clock = pygame.time.Clock()

    fruit_contours = FruitContours()

    fruits_on_screen = []

    pygame.init()

    # A dictionary for which buttons that will generate what fruit
    fruitdir = {K_UP: "banana", K_LEFT: "lemon", K_RIGHT: "apple"}

    while 1:
        screen.fill(black)

        delta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key

                # Let the user quit the fucking game
                if button == K_q:
                  return

                # Check if the player pressed a button
                if button in (K_UP,K_LEFT,K_RIGHT):
                    # if so: Create a new fruit
                    new_fruit = Fruit(fruitdir[button], default_speed)
                    fruits_on_screen.append(new_fruit)

        # Move and blit all the fruits on the screen
        for index, fruit in enumerate(fruits_on_screen):
          if fruit.move(delta):
            fruit.blit()
          else:
            fruits_on_screen.pop(index)

        # Randomly generate fruits (TODO: för att testa om det funkar)
        at_100_generate_fruit = random.randint(0, 100)
        if at_100_generate_fruit == 100:
            new_fruit = generateRandomFruit()
            fruits_on_screen.append(new_fruit)

        # Draw the fruit contours
        fruit_contours.blit()

        pygame.display.flip()

if __name__ == '__main__': main()
