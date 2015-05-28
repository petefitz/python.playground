import pygame, sys, time
import random
from decimal import *
import RPi.GPIO as GPIO
import time

from pygame.locals import *

pinA = 3
pinB = 5
pinC = 7
pinD = 8
pinE = 10
pinF = 11
pinG = 12
pinH = 13

pinButton = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)
GPIO.setup(pinC, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)
GPIO.setup(pinE, GPIO.OUT)
GPIO.setup(pinF, GPIO.OUT)
GPIO.setup(pinG, GPIO.OUT)
GPIO.setup(pinH, GPIO.OUT)

GPIO.setup(pinButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def displayNumber(num):
        GPIO.output(pinA, numbers[num][0])
        GPIO.output(pinB, numbers[num][1])
        GPIO.output(pinC, numbers[num][2])
        GPIO.output(pinD, numbers[num][3])
        GPIO.output(pinE, numbers[num][4])
        GPIO.output(pinF, numbers[num][5])
        GPIO.output(pinG, numbers[num][6])
        GPIO.output(pinH, numbers[num][7])

width = 1024
height = 768

pygame.init()

clock = pygame.time.Clock()

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)

colors = (BLACK, RED, GREEN, BLUE, YELLOW)
names = ('pete', 'mark')
#names = ('Hobbes', 'Cadbury', 'Donuts', 'Maple Syrup')

window = pygame.display.set_mode((width, height))
window.fill(WHITE)

sotwImg = pygame.image.load('sotw.png')
sotwImg = pygame.transform.scale(sotwImg, (height, height))
window.blit(sotwImg, ((width-height)/2, 0))

fontObj = pygame.font.Font('freesansbold.ttf', 48)
textSurfaceObj = fontObj.render('Click to pick Next Week !', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (width/2, height-40)
window.blit(textSurfaceObj, textRectObj)

pygame.display.update()

time.sleep(1)
countdown = 0
startTime = time.time()
repeatLoop = True
while repeatLoop:
        if time.time() - startTime > countdown:
                countdown+=1
                if countdown%2 == 0:
                        displayPattern(GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH, GPIO.HIGH)
                else:
                        displayPattern(GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH,  GPIO.HIGH, GPIO.LOW)
        
        if countdown == 10:
                repeatLoop = False
        if GPIO.input(pinButton) == GPIO.LOW:
                repeatLoop = False
        time.sleep(0.1)


fontObj = pygame.font.Font('freesansbold.ttf', 72)

startTime = time.time()
countdown = 0

repeatLoop = True
while repeatLoop:
        for event in pygame.event.get():
                if event.type == QUIT:
                        repeatLoop = False

        name = names[random.randint(0, len(names)-1)]
        forecolor = colors[random.randint(0, len(colors)-1)]
        backcolor = colors[random.randint(0, len(colors)-1)]
        if forecolor == backcolor:
                forecolor = WHITE
        textSurfaceObj = fontObj.render(name, True, forecolor, backcolor)
        textRectObj = textSurfaceObj.get_rect()

        coordx = random.randint(0, width)
        coordy = random.randint(0, height)
        textRectObj.center = (coordx, coordy)

        window.blit(textSurfaceObj, textRectObj)

        clock.tick(100)
        
        pygame.display.update()

        if time.time() - startTime > countdown:
                countdown+=1
        if countdown == 10:
                repeatLoop = False

        displayNumber(10 - countdown)


getcontext().prec = 2

sotwImg = pygame.image.load(name + '.jpg')
scale = Decimal(sotwImg.get_width()) / Decimal(sotwImg.get_height())

window.fill(WHITE)
pygame.display.update()

imgHeight = 10
while imgHeight < sotwImg.get_height():
        imgWidth = scale * imgHeight
        scaleImg = pygame.transform.scale(sotwImg, (imgWidth, imgHeight))
        window.blit(scaleImg, ((width-scaleImg.get_width())/2, (height-scaleImg.get_height())/2))
        imgHeight += 10

        pygame.display.update()
        clock.tick(30)

window.fill(WHITE)
window.blit(sotwImg, ((width-sotwImg.get_width())/2, (height-sotwImg.get_height())/2))

pygame.display.update()

repeatLoop = True
while repeatLoop:
        for event in pygame.event.get():
                if event.type == QUIT:
                        repeatLoop = False
        time.sleep(0.1)

pygame.quit()
