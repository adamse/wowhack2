import sys, os, pygame
from pygame.locals import *

size = width, height = 640, 700
screen = pygame.display.set_mode(size)

class Fruit:
    def __init__(self, image_name, speed):
        self.image = pygame.image.load(os.path.join('bilder', image_name + ".png"))
        self.rect = self.image.get_rect()
        self.rect.inflate(-4, -4)
        self.rect.midtop = (320, 0)
        self.speed = speed

    def blit(self):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect = self.rect.move((0, self.speed))

def main():
    black = 0, 0, 0
	
    default_speed = 3

    fruits_on_screen = []

    pygame.init()
    fruitdir = {K_UP: "banana", K_LEFT: "lemon", K_RIGHT: "apple"}

    while 1:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                name = pygame.key.name(button)	
                if button in (K_UP,K_LEFT,K_RIGHT):
                    new_fruit = Fruit(fruitdir[button], default_speed)
                    fruits_on_screen.append(new_fruit)

        for fruit in fruits_on_screen:
            fruit.move()
            fruit.blit()

        pygame.display.flip()

if __name__ == '__main__': main()
