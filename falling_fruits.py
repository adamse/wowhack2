import sys, os, pygame
from pygame.locals import *

## The size of the screen
size = width, height = 640, 700
## The screen is global, so the Fruit-class can get access to it
screen = pygame.display.set_mode(size)

class Fruit:
    def __init__(self, image_name, speed):
        ## Load the image and get the rect from the image
        self.image = pygame.image.load(os.path.join('bilder', image_name + ".png"))
        self.rect = self.image.get_rect()

        ## Resize the rect (TODO: verkade inte fungera)
        self.rect = self.rect.inflate(-4, -4)

        ## Make the fruit appear outside the screen at the top
        self.rect.midtop = (320, -100)
        
        ## The speed of which the fruit will fall
        self.speed = speed

    ## Blits the fruit to the screen
    def blit(self):
        screen.blit(self.image, self.rect)

    ## Moves the fruit according to the set speed
    def move(self):
        self.rect = self.rect.move((0, self.speed))

def main():
    black = 0, 0, 0
	
    ## The default speed for the generated fruits
    default_speed = 3

    fruits_on_screen = []

    pygame.init()

    ## A dictionary for which buttons that will generate what fruit
    fruitdir = {K_UP: "banana", K_LEFT: "lemon", K_RIGHT: "apple"}

    while 1:
        screen.fill(black)

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
        for fruit in fruits_on_screen:
            fruit.move()
            fruit.blit()

        pygame.display.flip()

if __name__ == '__main__': main()
