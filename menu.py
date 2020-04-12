from common import *

class Menu:
    topleft = 50, 50

    def __init__(self, name, screen, clock, title_size=150, item_size=50, title_color=WHITE, item_color=WHITE, item_spacing=20):
        self.name = name
        self.screen = screen
        self.clock = clock
        self.title_size = title_size
        self.item_size = item_size
        self.title_color = title_color
        self.item_color = item_color
        self.item_spacing = item_spacing
        self.items = []

    def add_item(self, name, color=(255, 255, 255)):
        self.items.append({"name":name, "color":color})

    def activate(self):
        while True:
            quit_handler()

            self.screen.fill((0, 0, 0))

            draw_text(self.name, self.screen, self.topleft, size=self.title_size, color=self.title_color)
            nextpos = self.topleft[0], self.topleft[1] + (self.item_spacing + self.title_size)
            for item in self.items:
                draw_text(item['name'], self.screen, nextpos, size=self.item_size, color=item['color'])
                nextpos = nextpos[0], nextpos[1] + (self.item_spacing + self.item_size)

            pygame.display.update()
            self.clock.tick(FPS)







