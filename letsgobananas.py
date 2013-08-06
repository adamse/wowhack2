import sys, os, pygame
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
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

class Fruit:
    def __init__(self, name, speed = 1):
        ## Load the image and get the rect from the image
        self.name = name
        self.image = pygame.image.load(os.path.join('bilder', name + ".png"))
        self.image = pygame.transform.scale(self.image,(50,50))         
        self.rect = self.image.get_rect()
        
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
    pygame.init()
    fruitdir = {K_UP: ('banana'),K_LEFT: ('lemon'), K_RIGHT: ('apple') }
    currentFruit = None    
    currentRect = None
    currentImg = None
    fruits = []
    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                if button == K_ESCAPE: return			
                elif button in (K_UP,K_LEFT,K_RIGHT):
                    name = pygame.key.name(button)
                    currentFruit = fruitdir[button]
                    new_fruit = Fruit(currentFruit)
                    fruits.append(new_fruit)                    
                    new_fruit.move()
                    pygame.display.flip()
                    print 'Well played, you pressed the ' + name + ' button!'					
                    print 'A wild ' + currentFruit + ' appeared!'
                else:
					print 'You fail!'
        for f in fruits :
            f.move()
            f.blit()				
            if f.rect.top < 0: 
                f.speed = - f.speed                
            elif f.rect.bottom > height:
                f.speed = - f.speed
                print 'An unfortunate ' + f.name + ' fell to the ground!'
        pygame.display.flip()				
if __name__ == '__main__': main()
