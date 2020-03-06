import pygame
import random
import sys
import os

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pygame.font.init()
length = 1024
height = 640
score = 100
currentMaxScore = score
deadScore = 0
maxScore = 0
addScore = 1
subScore = 1
limitRightNumber = 15
limitWrongNumber = 3

rightNumber = 0
wrongNumber = 0
number = 0

addScoreflag = 0
subScoreflag = 0
exitflag = 0



screen = pygame.display.set_mode((length,height))
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
px = {}
py = {}
used = []

def readScore():
    with open('score.txt','r') as r:
        maxScore = int(r.read())
        print(maxScore)
    return maxScore

def writeScore(maxScore):
    with open('score.txt', 'w') as w:
        w.write(str(maxScore))
        print(maxScore)



def drawText(screen, text, posx, posy, color, textsize = 40):
    fontObj = pygame.font.Font(None, textsize)
    textObj = fontObj.render(text, True, color)
    screen.blit(textObj,(posx,posy))

def loadDate():
    global maxScore
    if not os.path.isfile('score.txt'):
        with open('score.txt', 'w') as w:
            w.write('100')
    maxScore = readScore()


def draw(screen):

    drawText(screen, 'maxScore: ' + str(maxScore),10,10, white, 40)
    drawText(screen, 'Score: ' + str(score),10,40, white, 40)

def exit():
    if currentMaxScore > maxScore:
        writeScore(currentMaxScore)
    pygame.quit()
    sys.exit()

def dead():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()





def update(screen):
    global score,currentMaxScore,rightNumber,wrongNumber,addScore,subScore,addScoreflag,subScoreflag,exitflag
    screen.fill(black)
    draw(screen)
    number = random.randint(0, len(word) - 1)
    wd = word[number]

    if wd not in used:
        x = random.randint(10, length-10)
        y = -20
        used.append(wd)
        px[wd] = x
        py[wd] = y
        drawText(screen, word[number], x, y, white)

    for key, in py.keys():
        dy = 1.5
        dy = max(dy * score / 100,dy)
        py[key] += dy
        drawText(screen, key, px[key], py[key], white)

    pygame.display.set_caption("第一组 田野 打字游戏")

    if score <= 0:
        size = 200
        drawText(screen, 'Dead', length / 2 - size, height / 2 - size / 2, red, size)
        exitflag = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        ch = 0
        if event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[27] == 1:
                pygame.quit()
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
                rightNumber += 1
                wrongNumber = 0
                score += addScore
                currentMaxScore = max(score,currentMaxScore)
            else:
                wrongNumber += 1
                rightNumber = 0
                score -= subScore

    for i in range(len(py)):
        wd = word[i]
        if wd in used:
            if py[wd] > height:
                px.pop(wd)
                py.pop(wd)
                used.remove(wd)
                wrongNumber += 1
                rightNumber = 0
                score -= subScore

    if rightNumber == limitRightNumber and addScoreflag == 0:
        addScore *= 2
        addScoreflag = 1

    elif rightNumber < limitRightNumber:
        addScore = 1
        addScoreflag = 0


    if wrongNumber == limitWrongNumber and subScoreflag == 0:
        subScore *= 2
        subScoreflag = 1

    elif wrongNumber < limitWrongNumber:
        subScore = 1
        subScoreflag = 0


def main():
    loadDate()
    while True:
        update(screen)
        pygame.display.update()
        if exitflag == 1:
            break
    dead()

if __name__ == '__main__':
    main()