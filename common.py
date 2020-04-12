import random, sys
import pygame

FPS = 60
RES = HEIGHT, WIDTH = 800, 600
BLACK, WHITE, RED, GREEN, BLUE = [
    (0, 0, 0), 
    (255, 255, 255), 
    (255, 0, 0), 
    (0, 255, 0), 
    (0, 0, 255)
]


def ran_color():
    return (random.randint(0, 255) for _ in range(3))


def draw_text(text, surface, pos, font=None, size=20, color=(255,255,255)):
    if font is None:
        font = pygame.font.SysFont(None,size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = pos
    surface.blit(textobj, textrect)


def quit_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()