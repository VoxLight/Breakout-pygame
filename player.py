import pygame
import math


Paddle = pygame.Rect(
            pygame.display.get_surface().get_width()//2,
            pygame.display.get_surface().get_height()//8,
            20,
            4
        )
        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"./images/ball.jpg")
        self.rect = self.image.get_rect()
        self.pos = self.x, self.y = (
            pygame.display.get_surface().get_width()//2,
            pygame.display.get_surface().get_height()//8+self.rect.height
        )
    
    def collided_with_sprite(self, sprite):
        spos = sprite.rect.x, sprite.rect.y
        dist = math.sqrt(((self.x-spos[0])**2)+((self.y-spos[1])**2))
        return 

    def update(self):
        self.rect.center = self.pos

class Brick(pygame.sprite.Sprite):
    def __init__(self, pos, color='red'):
        pygame.sprite.Sprite.__init__(self)
        self.pos = self.x, self.y = pos
        self.color = color
        self.image = pygame.image.load(f"./images/bricks/{self.color}.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        

