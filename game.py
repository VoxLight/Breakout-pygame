# Initialise Pygame
import pygame
pygame.init()

from common import *
from pygame.locals import *

from menu import Menu
pygame.display.set_mode(resolutions[0], 0)

def update_resolution():
    current_res = pygame.display.get_surface().get_size()
    if resolutions.index(current_res) == len(resolutions) - 1:
        next_res = resolutions[0]
    else:
        next_res = resolutions[resolutions.index(current_res)+1]
    pygame.display.set_mode(next_res)

def update_mode(mode):
    pygame.display.set_mode(pygame.display.get_surface().get_size(), mode)


def main():
    
    # pygame setup
    pygame.display.set_caption("Breakout")
    CLOCK = pygame.time.Clock()

    

    # Setup menus for the game
    op = Menu('Options', pygame.display.get_surface(), CLOCK)

    op.add_item('Resolution', callback=update_resolution)
    op.add_item('Borderless', callback=lambda: update_mode(pygame.NOFRAME))
    op.add_item('Fullscreen', callback=lambda: update_mode(pygame.FULLSCREEN))
    op.add_item('Windowed', callback=lambda: update_mode(0))
    op.add_item('Back', callback='exit')


    mm = Menu('Main Menu', pygame.display.get_surface(), CLOCK)

    mm.add_item('New Game')
    mm.add_item('Level Select')
    mm.add_item('Stage Editor')
    mm.add_item('Options', callback=op.activate)
    mm.add_item('Quit', callback='exit')
    
    

    # main game loop
    mm.activate()

        

            
        


if __name__ == "__main__":
    main()



