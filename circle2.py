# CIRCLE DEMO
# By Jaseman - 22nd August 2012

import os, random, pygame; from pygame.locals import *
from math import sin, cos, pi 
pygame.init(); clock = pygame.time.Clock() 
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center' 
pygame.display.set_caption("Circle Demo") 
screen=pygame.display.set_mode((800,600),0,32)

bk=pygame.Surface((800,600)); bk.fill((0,64,0)) 
dot=pygame.Surface((4,4)); dot.set_colorkey([0,0,0]) 
pygame.draw.circle(dot,(255,255,255),(2,2),2,0)

smlradius = 60; bigradius = 120; points = 90
# Variable Arrays To Store X&Y points for a small and big circle 
smcx = []; smcy = []; bgcx = []; bgcy = []

# Calculate the X&Y points and put values into the array
angleStep = pi *2 / points
for a in range(0,points):
	smcx.append(sin(a * angleStep)*smlradius) 
	smcy.append(cos(a * angleStep)*smlradius) 
	bgcx.append(sin(a * angleStep)*bigradius) 
	bgcy.append(cos(a * angleStep)*bigradius)

a=0; b=0 # Points a & b will be moving points of the circles 
c=0; d=0 # Points for sine and cosine waves
cx=800/2; cy=600/2 # Centre of the screen
r=random.randint; pdl=pygame.draw.line # Abbreviations for commands

run = 1
while run == 1:

	screen.blit(bk,(0,0)) # Draw the background surface 
	screen.blit(dot,(cx-2,cy-2)) # Centrepoint

	# Draw the circle
	screen.blit(dot, (bgcx[a]+cx-2,bgcy[a]+cy-2)) 
	screen.blit(dot, (smcx[a]+cx-2,smcy[a]+cy-2)) 
	screen.blit(dot, (bgcx[b]+cx-2,bgcy[b]+cy-2)) 
	screen.blit(dot, (smcx[b]+cx-2,smcy[b]+cy-2)) 
	rcol=r(0,255); gcol=r(0,255); bcol=r(0,255)
	pdl(bk,[rcol,gcol,bcol],(bgcx[a]+cx-2,bgcy[a]+cy-2),(smcx[a]+cx-2,smcy[a]+cy-2))
	pdl(bk,[rcol,gcol,bcol],(bgcx[b]+cx-2,bgcy[b]+cy-2),(smcx[b]+cx-2,smcy[b]+cy-2))
	pdl(bk,[rcol,gcol,bcol],(smcx[a]+cx-2,smcy[a]+cy-2),(smcx[b]+cx-2,smcy[b]+cy-2))

	# Constrained points (Fixed X or Y) screen.blit(dot, (bgcx[a]+cx-2,cy-bigradius-14)) 
	screen.blit(dot, (bgcx[b]+cx-2,cy+bigradius+10)) 
	screen.blit(dot, (smcx[a]+cx-2,cy-bigradius-34)) 
	screen.blit(dot, (smcx[b]+cx-2,cy+bigradius+30)) 
	screen.blit(dot, (cx-bigradius-14,bgcy[a]+cy-2)) 
	screen.blit(dot, (cx-bigradius-34,smcy[a]+cy-2)) 
	screen.blit(dot, (cx+bigradius+14,bgcy[b]+cy-2)) 
	screen.blit(dot, (cx+bigradius+34,smcy[b]+cy-2)) 
	pdl(bk,[rcol,gcol,bcol],(bgcx[a]+cx-2,cy-bigradius-14),(smcx[a]+cx-2,cy-bigradius-34))
	pdl(bk,[rcol,gcol,bcol],(bgcx[b]+cx-2,cy+bigradius+10),(smcx[b]+cx-2,cy+bigradius+30))
	pdl(bk,[rcol,gcol,bcol],(cx-bigradius-14,bgcy[a]+cy-2),(cx-bigradius-34,smcy[a]+cy-2))
	pdl(bk,[rcol,gcol,bcol],(cx+bigradius+14,bgcy[b]+cy-2),(cx+bigradius+34,smcy[b]+cy-2))

	# Ellipse (Big and Small Radius points mixed) 
	screen.blit(dot, (bgcx[a]+cx-2+bigradius+160,smcy[a]+cy-2)) 
	screen.blit(dot, (smcx[a]+cx-2-bigradius-160,bgcy[a]+cy-2))

	screen.blit(dot, (cx-2+bigradius+160,cy-2)) 
	screen.blit(dot, (cx-2-bigradius-160,cy-2)) 
	pdl(bk,[rcol,gcol,bcol],(cx-2+bigradius+160,cy-2),(bgcx[a]+cx-2+bigradius+160,smcy[a]+cy-2))
	pdl(bk,[rcol,gcol,bcol],(cx-2-bigradius-160,cy-2),(smcx[a]+cx-2-bigradius-160,bgcy[a]+cy-2))

	# Sine and Cosine Waves
	screen.blit(dot, (c,smcy[a]+cy-2-bigradius-100))
	c=c+1
	if c>=800: c=0
	screen.blit(dot, (smcx[a]+cx-2-bigradius-100,d))
	d=d+1
	if d>=600: d=0

	clock.tick(200); pygame.display.update(); a=a-1; b=b+1
	if b>=points: b=0
	if a==-1: a=points-1
