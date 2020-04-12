# Initialise Pygame
import pygame
pygame.init()

from common import *
from pygame.locals import *

from menu import Menu




def main():
    
    # pygame setup
    pygame.display.set_caption("Breakout")
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(RES, pygame.RESIZABLE)

    # Setup menus for the game
    op = Menu('Options', SCREEN, CLOCK)

    op.add_item('Resolution')
    op.add_item('Back', callback='exit')


    mm = Menu('Main Menu', SCREEN, CLOCK)

    mm.add_item('New Game')
    mm.add_item('Level Select')
    mm.add_item('Stage Editor')
    mm.add_item('Options', callback=op.activate)
    mm.add_item('Quit', callback='exit')
    
    

    # main game loop
    mm.activate()

        

            
        


if __name__ == "__main__":
    main()



