import sys, os, pygame, random
from pygame.locals import *
"""
class Banana(something imagy) 
	def __init__(self):

class Apple(something imagy)
	def __init__(self):
class Lemon(something imagy)
	def __init__(self):
	def lemonparty(i):
"""
black = 0, 0, 0
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.init()
clock = pygame.time.Clock()

lemon_x = 85
banana_x = 299
apple_x = 512

class Fruit:
    def __init__(self, name, speed = 1.0):
        ## Load the image and get the rect from the image
        self.name = name
        self.image = pygame.image.load(os.path.join('bilder', name + ".png")).convert()
        self.image = pygame.transform.scale(self.image,(128,128))
        self.image.set_colorkey((255,255,255))         
        self.rect = self.image.get_rect()
        
        ## The speed of which the fruit will fall
        self.speed = speed
        self.x = 0
        if name == "lemon": self.pos = lemon_x
        elif name == "banana": self.pos = banana_x
        elif name == "apple": self.pos = apple_x
        self.rect.midtop = (self.pos,-100) 

    def blit(self):
        screen.blit(self.image, self.rect)

    def move(self,delta):
        self.rect = self.rect.move((0, self.speed*delta))

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
    fruit_contours = FruitContours()
    # timepoints = some function here that generates points.
    fruitdir = {K_UP: ('banana'),K_LEFT: ('lemon'), K_RIGHT: ('apple') }
    currentImg = None
    fruits = []
    timepoints= []
    start_time = pygame.time.get_ticks
    while True:
        # if (pygame.time.get_ticks-start_time) > timepoints[1]: spawn fruit and delete first element.      
        clock.tick(60)
        delta = (clock.get_time())
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                if button == K_ESCAPE: return			
                elif button in (K_UP,K_LEFT,K_RIGHT):
                    name = pygame.key.name(button)                    
                    for f in fruits:
                        if f.name == name: 
                            if (f.rect.bottom > (height - 128)):
                                print 'Well done, you saved the ' + f.name + '!'
                                fruits.remove(f)
                                break
                            else:
                            	print 'Fruit ' + name + ' not in range yet!'				
                else:
					print 'You fail!'
        for f in fruits :
            f.move(delta)
            f.blit()				                
            if f.rect.bottom > height:
                fruits.remove(f)
                print 'An unfortunate ' + f.name + ' fell through the ground and vanished!'

        if random.randint(0, 100) == 100:
            new_fruit = generateRandomFruit()
            fruits.append(new_fruit)
        fruit_contours.blit()
        pygame.display.flip()
        # if timepoints.len() < 1: end game				
if __name__ == '__main__': main()
