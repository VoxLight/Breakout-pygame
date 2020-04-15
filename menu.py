from common import *
import pygame
import sys

from audio import Audio

class Menu:
    topleft = 50, 50

    def __init__(self, name, clock, title_size=150, title_color=WHITE, item_size=50, item_spacing=20):
        self.name = name
        self.clock = clock
        self.title_size = title_size
        self.item_size = item_size
        self.title_color = title_color
        self.item_spacing = item_spacing
        self.items = []
        self.is_active = False
        self.audio = Audio()

    def add_item(self, name, color=WHITE, callback=lambda: True):
        self.items.append({"name":name, "color":color, "callback":callback})

    def activate(self):
        screen = pygame.display.get_surface()
        self.is_active = True
        selected = 0
        #TODO: Make this event loop more concise
        # and easier to expand upon in the future
        while self.is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.audio.play_select()
                        if selected == 0:
                            selected = len(self.items)-1
                        else:
                            selected -= 1
                    elif event.key == pygame.K_DOWN:
                        self.audio.play_select()
                        if selected == len(self.items)-1:
                            selected = 0
                        else:
                            selected += 1
                    if event.key == pygame.K_RETURN:
                        self.audio.play_brick_collide()
                        action = self.items[selected]["callback"]
                        if type(action) == str:
                            if action == "exit":
                                self.is_active = False
                                break
                        else:
                            action()
                        

            screen.fill(BLACK)

            draw_text(self.name, self.topleft, size=self.title_size, color=self.title_color)
            nextpos = self.topleft[0], self.topleft[1] + (self.item_spacing + self.title_size)
            for item in self.items:
                if self.items.index(item) == selected:
                    text = "-> " + item['name']
                else:
                    text = item['name']
                draw_text(text, nextpos, size=self.item_size, color=item['color'])
                nextpos = nextpos[0], nextpos[1] + (self.item_spacing + self.item_size)

            

            pygame.display.update()
            self.clock.tick(FPS)

