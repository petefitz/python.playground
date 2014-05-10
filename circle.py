# POINTS OF A CIRCLE
# By Jaseman 21st August 2012

import os, pygame;
from pygame.locals import *
from math import sin, cos, pi

pygame.init();
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Points Of A Circle")
screen=pygame.display.set_mode((600,600),0,32)

background=pygame.Surface((600,600))
background.fill((0,0,192))

dot=pygame.Surface((8,8))
pygame.draw.circle(dot,(255,255,255),(4,4),4,0)
dot.set_colorkey([0,0,0])

screen.blit(background,(0,0))
screen.blit(dot,(300-4,300-4))

# Paste a dot in the centre of the screen
# 300=half screen width 4=half dot width
radius = 200
points = 90
angleStep = pi *2 / points

for a in range(0,points):
    x = sin(a*angleStep)*radius
    y = cos(a*angleStep)*radius
    screen.blit(dot,(x+300-4, y+300-4))
    
# Paste dots in a circle
pygame.display.update()
pygame.time.wait(30000)
