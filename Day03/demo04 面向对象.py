import pygame as pg
import sys
import random

vec = pg.math.Vector2
ball_img = 'ball.png'

WIDTH = 1024
HEIGHT = 640
black = (0,0,0)
BALL_NUMBER = 20



class ball(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.balls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.ball_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.xspeed = random.random() * 2
        self.yspeed = random.random() * 2




    def update(self):
        if self.x > WIDTH or self.x < 0:
            self.xspeed = - self.xspeed
        if self.y > HEIGHT or self.y < 0:
            self.yspeed = - self.yspeed
        self.x += self.xspeed
        self.y += self.yspeed



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.ball_img = pg.image.load('ball.png')

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        for i in range(0,BALL_NUMBER):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            ball(self, x, y)


    def quit(self):
        pg.quit()
        sys.exit(0)

    def update(self):
        self.all_sprites.update()


    def run(self):
        self.playing = True
        while self.playing:
            self.update()
            self.events()
            self.update()
            self.draw()

    def draw(self):
        pg.display.set_caption("第一组 田野 小球")
        self.screen.fill(black)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.x,sprite.y))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
def main():
    try:
        g = Game()
        g.new()

        while True:
            g.run()
    except SystemError:
        pass

if __name__ == '__main__':
    main()
