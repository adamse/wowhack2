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
	size = width, height = 320, 240
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	
	lemon = pygame.image.load(os.path.join('bilder','lemon.png'))
	lemonrect = lemon.get_rect()

	apple = pygame.image.load(os.path.join('bilder','apple.png'))
	applerect = apple.get_rect()

	banana = pygame.image.load(os.path.join('bilder','banana.png'))
	bananarect = banana.get_rect()
	
	pygame.init()
	fruitdir = {K_UP: 'banana',K_LEFT: 'lemon', K_RIGHT: 'apple' }
        imgdir = {K_UP: banana, K_LEFT: lemon, K_RIGHT: apple}
	rectdir = {K_UP: bananarect ,K_LEFT: lemonrect , K_RIGHT: applerect }
	while 1:
		for event in pygame.event.get():
        		if event.type == QUIT: return
			elif event.type == KEYDOWN:
				button = event.key
				name = pygame.key.name(button)			
				if button in (K_UP,K_LEFT,K_RIGHT):
					screen.fill(black)
					screen.blit(imgdir[button],rectdir[button])
                                        pygame.display.flip()
					print 'Well played, you pressed the ' + name + ' button!'					
					print 'A wild ' + fruitdir[button] + ' appeared!'
				else:
					print 'You fail!'					

if __name__ == '__main__': main()
