# GRADIENT FILL
# By Jaseman 8th August 2012

import os, pygame;
from pygame.locals import *

pygame.init(); clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Gradient Fill")
screen=pygame.display.set_mode([600,382],0,32)

# We know that color values are between 0-255 so...
# Lets give the sky surface 255 pixels height
sky = pygame.Surface((600,255))

# Now we will draw rectangles down from the top of the sky surface
# Each rectangle gets slightly higher color values so that the blue
# gets lighter and lighter towards the horizon
# We will define some variables and then create a loop to draw
# rectangles

r=0; g=64; b=128 # Start Red Green and Blue Values

for l in range (0,255):
    pygame.draw.rect(sky,(r,g,b),(0,l-1,600,l))
    r=r+1;g=g+1;b=b+1 # Increase the Red Green and Blue Values
    if r>=255: r=255 # Max amount of red allowed
    if g>=255: g=255 # Max amount of green allowed
    if b>=255: b=255 # Max amount of blue allowed
    
# Let's do a similar thing with the ground
# For the ground let's have half as many pixels height
# as available color values (256/2=128)

ground = pygame.Surface((600,128))

r=192; g=255; b=192 # Start Red Green and Blue Values

for l in range (0,128):
    pygame.draw.rect(ground,(r,g,b),(0,l-2,600,l))
    r=r-2; g=g-2; b=b-2
    # Decrease the Red Green and Blue Values
    if r<=0: r=0 # Min amount of red allowed
    if g<=0: g=0 # Min amount of green allowed
    if b<=0: b=0 # Min amount of blue allowed
    
screen.blit(sky,(0,0)) # Paste the sky surface onto the screen
screen.blit(ground,(0,255)) # Paste the ground surface onto the screen
pygame.display.update()

pygame.time.wait(10000) # A 10 second pause before the program ends
