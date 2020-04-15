import pygame

import json

import player

from common import *
from player import *
from audio import Audio



class Level:

    def __init__(self, clock, fp=level_files[0], level_select=False):
        self.fp = fp
        self.clock = clock
        self.sound = Audio()

        self.is_active = False
        self.is_loaded = False
        self.is_level_select = level_select

        self.bricks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()

        self.paddle = player.Paddle()
        self.ball = player.Ball()
        self.balls.add(self.ball)
        self.ball.rect.center = self.paddle.rect.center
        self.ball.rect.y-=self.ball.rect.height

        

    def activate(self):
        if not self.is_loaded:
            self.load()

        screen = pygame.display.get_surface()
        self.is_active = True

        self.ball.velocity = 0,self.ball.speed
        
        while self.is_active:
            # Check to see if the user has beat the stage and start the next level
            if not self.is_level_select:
                if len(self.bricks.sprites()) == 0:
                    if level_files.index(self.fp) == len(level_files) - 1:
                        self.is_active = False
                        self.is_loaded = False
                        self.bricks = pygame.sprite.Group()
                        break
                    self.fp = level_files[level_files.index(self.fp)+1]
                    self.load()
            else:
                if len(self.bricks.sprites()) == 0:
                    self.is_active = False
                    self.is_loaded = False
                    self.bricks = pygame.sprite.Group()
                    break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.bricks.empty()
                        self.is_active = False
                        break

            # Handle Paddle Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.rect.x -= 5 # Move paddle left

            elif keys[pygame.K_RIGHT]:
                self.paddle.rect.x += 5 # Move paddle right

            b_col = pygame.sprite.spritecollide(self.ball, self.bricks, False)

            if pygame.sprite.spritecollide(self.paddle, self.balls, False):
                diff = (self.paddle.rect.x + self.paddle.rect.width/2) - (self.ball.rect.x+self.ball.rect.width/2)
                self.ball.bounce_v(diff)
                self.sound.play_paddle_collide()
                # self.ball.rect.y = HEIGHT - self.paddle.rect.height - self.ball.rect.height - 1
                
            
            elif len(b_col) > 0:
                if self.ball.rect.y <= b_col[-1].rect.y - (b_col[-1].rect.height/2):
                    # Hit was above
                    self.ball.bounce_v(0)
                    self.sound.play_brick_collide()
                    

                elif self.ball.rect.y >= b_col[-1].rect.y + (b_col[-1].rect.height/2):
                    # Hit was below
                    self.ball.bounce_v(0)
                    self.sound.play_brick_collide()

                if self.ball.rect.x < b_col[-1].rect.x:
                    # Hit was left
                    self.ball.bounce_h(0)
                    self.sound.play_brick_collide()
                    

                elif self.ball.rect.x > b_col[-1].rect.x:
                    # Hit was right
                    self.ball.bounce_h(0)
                    self.sound.play_brick_collide()

                # self.ball.bounce(0)
                
                b_col[-1].kill()



            screen.fill(BLACK)

            # draw the blocks in the level
            self.bricks.draw(screen)

            # draw the paddle
            pygame.draw.rect(screen, WHITE, self.paddle.rect)


            # update and draw the ball
            self.ball.update()
            self.ball.draw()

            screen.blit(self.ball.image, self.ball.rect)
            

            

            pygame.display.update()
            self.clock.tick(FPS)

    def load(self):
        with open(self.fp, 'r') as f:
            load = json.load(f)['bricks']

        for brick in load:
            self.bricks.add(Brick((brick['x'], brick['y']), brick['color']))

        self.is_loaded = True


