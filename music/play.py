import os
import sys
import pygame

if len(sys.argv) < 2:
  sys.exit("Please supply a music file: " + argv[0] + " [FILE]")

if not os.path.exists(sys.argv[1]):
  sys.exit("File not found.")


pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound(sys.argv[1])
sound.play()

clock = pygame.time.Clock()

while 1:
  clock.tick(10)
