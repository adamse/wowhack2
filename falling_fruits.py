# vim: set fileencoding=utf8

import sys, os, pygame
from pygame.locals import *

## The size of the screen
size = width, height = 640, 700
## The screen is global, so the Fruit-class can get access to it
screen = pygame.display.set_mode(size)

class Fruit:
    def __init__(self, image_name, speed):
        ## Load the image and get the rect from the image
        self.image = pygame.image.load(os.path.join('bilder', image_name + ".png")).convert()

        ## Set white to the transparent color
        self.image.set_colorkey((0, 0, 0))

        ## Resize the image
        self.image = pygame.transform.scale(self.image, (128, 128))
#        self.rect = self.rect.inflate(-20, -20) ## this doesn't work now and I'm not sure why

        self.rect = self.image.get_rect()

        ## This is a bit ugly, but...
        ## Determine the x coordinate of the fruit according to which fruit it is
        ## TODO: Jag fattar inte dessa siffror (de verkar inte vara koordinater?
        ##       fast de borde bero på recten och jag tror inte jag lyckas resizea den)
        if image_name == "lemon":
            self.x = 85
        elif image_name == "banana":
            self.x = 299
        if image_name == "apple":
            self.x = 512

        ## Make the fruit appear outside the screen at the top
        self.rect.midtop = (self.x, -100)

        ## The speed of which the fruit will fall
        self.speed = speed

    ## Blits the fruit to the screen
    def blit(self):
        screen.blit(self.image, self.rect)

    ## Moves the fruit according to the set speed and the time delta
    ## (this is so the fruit moves to actual time passed, which could differ for every iteration of the game loop)
    ## returns True if were still on screen
    def move(self, delta):
        self.rect = self.rect.move((0, self.speed * delta))
        return (self.rect.y <= height)


def main():
    black = 0, 0, 0

    clock = pygame.time.Clock()

    ## The default speed for the generated fruits
    default_speed = 0.5

    fruits_on_screen = []

    pygame.init()

    ## A dictionary for which buttons that will generate what fruit
    fruitdir = {K_UP: "apple", K_LEFT: "lemon", K_RIGHT: "banana"}

    while 1:
        screen.fill(black)

        delta = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                ## Check if the player pressed a button
                if button in (K_UP,K_LEFT,K_RIGHT):
                    ## if so: Create a new fruit
                    new_fruit = Fruit(fruitdir[button], default_speed)
                    fruits_on_screen.append(new_fruit)

        ## Move and blit all the fruits on the screen
        for index, fruit in enumerate(fruits_on_screen):
          if fruit.move(delta):
            fruit.blit()
          else:
            fruits_on_screen.pop(index)

        pygame.display.flip()

if __name__ == '__main__': main()
