import pygame
import player
import json, sys, math
from tkinter import Tk, filedialog


from common import *
from player import Brick


# from https://stackoverflow.com/questions/39252088/pygame-snap-mouse-to-grid
def draw_grid(spacing):
    surface = pygame.display.get_surface()
    width, height = surface.get_size()
    for x in range(0, width, spacing):
        pygame.draw.line(surface, WHITE, (x,0), (x, height))
    for y in range(0, height, spacing):
        pygame.draw.line(surface, WHITE, (0,y), (width, y))


# from https://www.geeksforgeeks.org/round-the-given-number-to-nearest-multiple-of-10/
def round_num(n, nearest=10):
    a = (n // nearest) * nearest
    b = a + nearest 
    return (b if n - a > b - n else a) 


def round_coords(pos, nearest=10):
    return (round_num(pos[0], nearest), round_num(pos[1], nearest))


class LevelEditor:

    def __init__(self, clock, file=None):
        self.is_active = False
        self.clock = clock
        self.bricks = pygame.sprite.Group()
        self.brick_colors = [
            'red', 'orange', 'yellow', 
            'green', 'blue', 'pink', 'purple'
        ]


    def activate(self):
        screen = pygame.display.get_surface()
        self.is_active = True
        selected = 0
        placement_block = Brick((0, 0), self.brick_colors[selected])
        while self.is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if selected == len(self.brick_colors)-1:
                            selected = 0
                        else:
                            selected += 1
                        placement_block = Brick((0, 0), self.brick_colors[selected])

                    elif event.key == pygame.K_DOWN:
                        if selected == 0:
                            selected = len(self.brick_colors)-1
                        else:
                            selected -= 1
                        placement_block = Brick((0, 0), self.brick_colors[selected])
                    elif event.key == pygame.K_s:
                        self.save()
                    elif event.key == pygame.K_d:
                        self.load()
                    elif event.key == pygame.K_q:
                        self.bricks.empty()
                        self.is_active = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        for brick in reversed(list(self.bricks)):
                            if brick.rect.collidepoint(pygame.mouse.get_pos()):
                                brick.kill()
                                break

                    elif event.button == 1:
                        self.bricks.add(Brick(
                            round_coords(pygame.mouse.get_pos(), 
                            placement_block.rect.width//2), 
                            self.brick_colors[selected]
                            ))

            screen.fill(BLACK)
            # get a snapped cord

            draw_grid(placement_block.rect.width-1)

            # draw the placed blocks
            self.bricks.draw(screen)

            # draw the block to place.
            placement_block.rect.center = round_coords(pygame.mouse.get_pos(), placement_block.rect.width//2)
            screen.blit(placement_block.image, placement_block.rect)

            

            pygame.display.update()
            self.clock.tick(FPS)

            

    def save(self):
        root = Tk()
        fp = filedialog.asksaveasfilename(
            initialdir="./levels",
            filetypes=[("Json", "*.json"), ("All", "*.*")])
        if not fp:
            return
        _save = {
            "bricks":[
                {
                    'x':brick.rect.center[0], 
                    'y':brick.rect.center[1], 
                    'color':brick.color
                } for brick in self.bricks
            ]
            
        }
        with open(fp, 'w+') as f:
            json.dump(_save, f)
            root.destroy()


    def load(self):
        root = Tk()
        fp = filedialog.askopenfilename(
            initialdir="./levels",
            filetypes=[("Json", "*.json"), ("All", "*.*")])
        if not fp:
            return
        with open(fp, 'r') as f:
            load = json.load(f)['bricks']
            root.destroy()

        for brick in load:
            self.bricks.add(Brick((brick['x'], brick['y']), brick['color']))
        


class Level:
    def __init__(self, file):
        self.bricks = pygame.sprite.Group()
        self.paddle = player.Paddle
        self.ball = player.Ball()
        with open(file) as f:
            level_data = json.load(f)
        for brick in level_data:
            self.bricks.add(player.Brick((brick['x'],brick['y']), brick['color']))


