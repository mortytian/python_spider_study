import pygame as pg
import sys
screen = pg.display.set_mode((620,400))

backgroundImage = 'images/background.png'
earthImage = 'images/blackMoon.png'
moonImage = 'images/whiteMoon.png'

background = pg.image.load(backgroundImage)
earth = pg.image.load(earthImage)
moon = pg.image.load(moonImage)

earth_x = 400

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    screen.blit(background,(0,0))
    screen.blit(moon, (50,100))
    screen.blit(earth,(earth_x,100))
    earth_x -= 2
    pg.display.update()
