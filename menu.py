from common import *
import pygame
import sys

class Menu:
    topleft = 50, 50

    def __init__(self, name, screen, clock, title_size=150, title_color=WHITE, item_size=50, item_spacing=20):
        self.name = name
        self.screen = screen
        self.clock = clock
        self.title_size = title_size
        self.item_size = item_size
        self.title_color = title_color
        self.item_spacing = item_spacing
        self.items = []
        self.is_active = False

    def add_item(self, name, color=WHITE, callback=lambda: True):
        self.items.append({"name":name, "color":color, "callback":callback})

    def activate(self):
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
                        if selected == 0:
                            selected = len(self.items)-1
                        else:
                            selected -= 1
                    elif event.key == pygame.K_DOWN:
                        if selected == len(self.items)-1:
                            selected = 0
                        else:
                            selected += 1
                    if event.key == pygame.K_RETURN:
                        action = self.items[selected]["callback"]
                        if type(action) == str:
                            if action == "exit":
                                self.is_active = False
                                break
                        else:
                            action()
                        

            self.screen.fill((0, 0, 0))

            draw_text(self.name, self.screen, self.topleft, size=self.title_size, color=self.title_color)
            nextpos = self.topleft[0], self.topleft[1] + (self.item_spacing + self.title_size)
            for item in self.items:
                if self.items.index(item) == selected:
                    text = "-> " + item['name']
                else:
                    text = item['name']
                print(item['color'])
                draw_text(text, self.screen, nextpos, size=self.item_size, color=item['color'])
                nextpos = nextpos[0], nextpos[1] + (self.item_spacing + self.item_size)

            

            pygame.display.update()
            self.clock.tick(FPS)







