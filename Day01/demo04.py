import pygame
import random
import sys
screen = pygame.display.set_mode((620,400))

backgroundImage = 'images/background.png'
starImage = 'images/star202.png'

background = pygame.image.load(backgroundImage)
star = pygame.image.load(starImage)

y = 10
x =[]
y =[]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    nx = random.randint(0,620)
    x.append(nx)
    y.append(-20.1)


    for i in range(len(x)):
        screen.blit(star,(x[i],y[i]))
        y[i] +=  2
    for i in range(len(y) -1):
        if y[i] > 420:
            y.pop(i)
            x.pop(i)
    pygame.display.update()

