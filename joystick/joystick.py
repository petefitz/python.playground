import os, pygame
from pygame.locals import *

pygame.init()

# set the width and height of the screen
size = [640, 640]
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# give the window a title
pygame.display.set_caption("Joystick Ball")

# This makes the normal mouse pointer invisible in graphics window
pygame.mouse.set_visible(0)

white_surf = pygame.Surface((610, 610))
whiterect = white_surf.get_rect()
whiterect.left = 15
whiterect.top = 15
whitebackground = pygame.draw.rect(white_surf, white, (0, 0, 610, 610))

# create surfaces for the bat and ball
ball_surf = pygame.Surface((30,30))
ballrect = ball_surf.get_rect()
ball_surf.fill(white)
ball = pygame.draw.circle(ball_surf, red, [15, 15], 15)

# loop until the user clicks the close button
done=0

# create a timer to control how often the screen updates
clock = pygame.time.Clock()

xPos = 305
yPos = 305

#let's see the end result
while done == 0:
    screen.fill(black)

    # event handling
    for event in pygame.event.get(): # if we click something ...
        if event.type == pygame.QUIT: # if we click close ...
            done=1 # this will cause the loop to finish.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=1 # Be IDLE friendly!

    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        xPos-=1
        if xPos==14:
            xPos=15
    if keys[K_RIGHT]:
        xPos+=1
        if xPos==596:
            xPos=595
    if keys[K_UP]:
        yPos-=1
        if yPos==14:
            yPos=15
    if keys[K_DOWN]:
        yPos+=1
        if yPos==596:
            yPos=595

    ballrect.left = xPos
    ballrect.top = yPos

    screen.blit(white_surf, whiterect)
    screen.blit(ball_surf, ballrect)

    # set the loop to 60 cycles per second
    clock.tick(60)

    # update the display
    pygame.display.flip()

pygame.quit()
