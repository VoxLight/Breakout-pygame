# Initialise Pygame
import pygame
pygame.init()

from common import *
from pygame.locals import *

from menu import Menu


def main():
    
    # pygame setup
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption("Breakout")

    SCREEN = pygame.display.set_mode(RES, pygame.RESIZABLE)
    
    # Setup menus for the game
    mm = Menu('Main Menu', SCREEN, CLOCK)
    # TODO: Add Menu.activate as callback for these items
    mm.add_item('New Game')
    mm.add_item('Level Select')
    mm.add_item('Stage Editor')
    mm.add_item('Options')
    mm.add_item('Quit', callback='exit')

    # main game loop
    while True:
        mm.activate()

        

            
        


if __name__ == "__main__":
    main()



