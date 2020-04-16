import pygame
import math

from common import *


class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            pygame.display.get_surface().get_width()//2,
            pygame.display.get_surface().get_height()-(pygame.display.get_surface().get_height()//8),
            120,
            6
        )
        self.speed = 5

        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"./images/ball.jpg")
        self.rect = self.image.get_rect()
        self.crash = False
        self.direction = 200
        self.speed = 5


    def bounce_v(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def bounce_h(self, diff):
        self.direction = (360 - self.direction) % 360
        self.direction -= diff
    

    def update(self):
        direction_radians = math.radians(self.direction)

        self.rect.x -= self.speed * math.sin(direction_radians)
        self.rect.y += self.speed * math.cos(direction_radians)

        # Do we bounce off the top of the screen?
        if self.rect.y <= 0:
            self.bounce_v(0)
            self.rect.y = 1

        # Do we bounce off the left of the screen?
        if self.rect.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.rect.x = 1

        # Do we bounce off the right side of the screen?
        if self.rect.x >= WIDTH - self.rect.width:
            self.direction = (360 - self.direction) % 360
            self.x = WIDTH - self.rect.width - 1

        # Did we fall off the bottom edge of the screen?
        if self.rect.y >= HEIGHT:
            self.crash = True

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.rect)

class Brick(pygame.sprite.Sprite):
    def __init__(self, pos, color='red'):
        pygame.sprite.Sprite.__init__(self)
        self.pos = self.x, self.y = pos
        self.color = color
        self.image = pygame.image.load(f"./images/bricks/{self.color}.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.rect)
        

