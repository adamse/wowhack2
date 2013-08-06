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
def main():
    speed = [0,-1]
    size = width, height = 640, 480
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
	
    lemon = pygame.image.load(os.path.join('bilder','lemon.png'))
    lemon = pygame.transform.scale(lemon,(50,50))	
    lemonrect = lemon.get_rect()

    apple = pygame.image.load(os.path.join('bilder','apple.png'))
    apple = pygame.transform.scale(apple,(50,50))	
    applerect = apple.get_rect()

    banana = pygame.image.load(os.path.join('bilder','banana.png'))
    banana = pygame.transform.scale(banana,(50,50))
    bananarect = banana.get_rect()
	
    pygame.init()
    fruitdir = {K_UP: ('banana',banana,bananarect),K_LEFT: ('lemon',lemon,lemonrect), K_RIGHT: ('apple',apple,applerect) }
    currentFruit = None    
    currentRect = None
    currentImg = None
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT: return
            elif event.type == KEYDOWN:
                button = event.key
                if button == K_ESCAPE: return			
                elif button in (K_UP,K_LEFT,K_RIGHT):
                    name = pygame.key.name(button)
                    (currentFruit,currentImg,currentRect) = fruitdir[button]
                    screen.fill(black)
                    screen.blit(currentImg,currentRect)
                    pygame.display.flip()
                    print 'Well played, you pressed the ' + name + ' button!'					
                    print 'A wild ' + currentFruit + ' appeared!'
                else:
					print 'You fail!'
        if currentFruit is not None:
            currentRect = currentRect.move(speed)
            screen.fill(black)
            screen.blit(currentImg,currentRect)				
            pygame.display.flip()
            if currentRect.top < 0: 
                speed[1] = -speed[1]                
            elif currentRect.bottom > height:
                speed[1] = -speed[1]
                print 'An unfortunate ' + currentFruit + ' dropped to the ground!'				
if __name__ == '__main__': main()
