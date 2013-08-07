import sys, os, pygame, random

class Background:
  def __init__(self, screen, width, height):
    self.width = width; self.height = height
    self.screen = screen
    self.one = self.fo("space1")
    self.two = self.fo("space2")
    self.three = self.fo("space3")

  def fo(self, image):
    im = pygame.image.load(os.path.join("bilder", image + ".png")).convert()
    im = pygame.transform.scale(im, (self.width, self.width))
    im.set_colorkey((0,0,0))
    return im

  def move(self):
    return

  def blit(self):
    self.screen.blit(self.one, (0, 0))
    self.screen.blit(self.two, (0, 0))
    self.screen.blit(self.three, (0, 0))
