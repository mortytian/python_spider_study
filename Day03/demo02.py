import pygame
import random
import sys

black = (0,0,0)
white = (255,255,255)
pygame.font.init()
length = 1024
height = 640
screen = pygame.display.set_mode((length,height))

word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
px = {}
py = {}
used = []

def drawText(screen, text, posx, posy, color, textsize = 40):
    fontObj = pygame.font.Font(None, textsize)
    textObj = fontObj.render(text, True, color)
    screen.blit(textObj,(posx,posy))

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ch = 0
        if event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[27] == 1:
                sys.exit()
            for i in range(97,123):
                if change[i] == 1:
                    ch = i - 97
                    break
            wd = word[ch]
            if wd in used:
                px.pop(wd)
                py.pop(wd)
                used.remove(wd)
    for i in range(len(py)):
        wd = word[i]
        if wd in used:
            if py[wd] > height:
                px.pop(wd)
                py.pop(wd)
                used.remove(wd)

while True:
    update()
    screen.fill(black)
    pygame.display.set_caption("第一组 田野 字母雨")
    number = random.randint(0, len(word) -1)
    wd = word[number]
    if wd not in used:
        x = random.randint(0,length)
        y = -20
        used.append(wd)
        px[wd] = x
        py[wd] = y
        drawText(screen, word[number],x,y,white)

    for key, in py.keys():
        dy = 1.5
        py[key] += dy
        drawText(screen, key ,px[key],py[key],white)

    pygame.display.update()