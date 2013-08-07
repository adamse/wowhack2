import sys, os, pygame, random

class Background:
  def __init__(self, screen, width, height):
    self.width = width; self.height = height
    self.screen = screen
    self.one = self.fo("space1")
    self.two = self.fo("space2")
    self.three = self.fo("space3")

    self.oney = 0
    self.twoy = 100
    self.threey = 500

  def fo(self, image):
    im = pygame.image.load(os.path.join("bilder", image + ".png")).convert()
    im = pygame.transform.scale(im, (self.width, self.width))
    im.set_colorkey((0,0,0))
    return im

  def move(self):
    self.oney -= 5
    if self.oney < -self.width:
      self.oney = 0
    self.twoy -= 7
    if self.twoy < -self.width:
      self.twoy = 0
    self.threey -= 10
    if self.threey < -self.width:
      self.threey = 0

  def blit(self):
    self.move()
    for offset in (0, self.width, 2*self.width):
      self.screen.blit(self.one, (0, self.oney + offset))
      self.screen.blit(self.two, (0, self.twoy + offset))
      self.screen.blit(self.three, (0, self.threey + offset))
