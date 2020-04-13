import pygame
class Paddle:
    def __init__(self):
        pass

class Ball:
    def __init__(self):
        pass

class Game:

    def __init__(self):
        ds = pygame.display.get_surface().get_size()
        self.paddle_pos = ds[0]-(ds[0]//8)
        self.ball_pos = self.ball_x, self.ball_y = ds[0]//2, ds[1]//2
        

