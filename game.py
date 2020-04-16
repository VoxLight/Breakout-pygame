# Initialise Pygame
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
from pygame.locals import *

from tkinter import Tk, filedialog

pygame.display.set_mode((800, 600), 0)
from common import *



from menu import Menu
from audio import Audio
from level_editor import LevelEditor
from level import Level



def new_level(clock):
    Level(clock).activate()


def level_select(clock):
    root = Tk()
    fp = filedialog.askopenfilename(
        initialdir="./levels",
        filetypes=[("Json", "*.json"), ("All", "*.*")]
    )
    root.destroy()
    if not fp:
        return
    Level(clock, fp, level_select=True).activate()


def play_intro_sequence(clock, sound):
    screen = pygame.display.get_surface()

    title_card = pygame.image.load("./images/Title.png").convert()
    
    # Play Title sound
    sound.play_music_title()

    # Fade in
    print("Start Fade In")
    for alpha in range(0, 300,):
        title_card.set_alpha(alpha)
        screen.fill(BLACK)
        screen.blit(title_card, screen.get_rect())
        pygame.display.update()
        pygame.time.delay(5)



    # Fade out
    for alpha in range(300, 0, -1):
        title_card.set_alpha(alpha)
        screen.fill(BLACK)
        screen.blit(title_card, screen.get_rect())
        pygame.display.update()
        pygame.time.delay(5)

        

def update_mode(mode):
    pygame.display.set_mode(pygame.display.get_surface().get_size(), mode)


def main():
    
    # pygame setup
    pygame.display.set_caption("Breakout")

    CLOCK = pygame.time.Clock()
    AUDIO = Audio()

    play_intro_sequence(CLOCK, AUDIO)

    AUDIO.play_music_main()
    

    

    # Setup menus for the game


    op = Menu('Options', CLOCK)

    op.add_item('Borderless', callback=lambda: update_mode(pygame.NOFRAME))
    op.add_item('Fullscreen', callback=lambda: update_mode(pygame.FULLSCREEN))
    op.add_item('Windowed', callback=lambda: update_mode(0))
    op.add_item('Back', callback='exit')


    mm = Menu('Main Menu', CLOCK)

    mm.add_item('New Game', callback=lambda: new_level(CLOCK))
    mm.add_item('Level Select', callback=lambda: level_select(CLOCK))
    mm.add_item('Stage Editor', callback=LevelEditor(CLOCK).activate)
    mm.add_item('Options', callback=op.activate)
    mm.add_item('Quit', callback='exit')
    
    

    # main game loop
    mm.activate()

        

            
        


if __name__ == "__main__":
    main()



