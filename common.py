import random, sys, glob
import pygame

FPS = 60

BLACK, WHITE, RED, GREEN, BLUE = [
    (0, 0, 0), 
    (255, 255, 255), 
    (255, 0, 0), 
    (0, 255, 0), 
    (0, 0, 255)
]

level_files = [fp for fp in glob.glob("./levels/base_stages/level_*.json")]

RES = WIDTH, HEIGHT = pygame.display.get_surface().get_size()




# from https://forum.processing.org/one/topic/recreate-map-function.html
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


def ran_color():
    return (random.randint(0, 255) for _ in range(3))


def draw_text(text, pos, font=None, size=20, color=WHITE):
    if font is None:
        font = pygame.font.SysFont(None,size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = pos
    pygame.display.get_surface().blit(textobj, textrect)
