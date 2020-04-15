import pygame


class Audio:
    _fp_effect_menu_select = "./sounds/effects/menu_select.wav"
    _fp_effect_brick_collide = "./sounds/effects/brick_collide.wav"
    _fp_effect_paddle_collide = "./sounds/effects/paddle_collide.wav"

    _fp_music_main = "./sounds/music/main.wav"
    _fp_music_title = "./sounds/music/title.wav"

    def __init__(self):
        # SFX
        self.menu_select = pygame.mixer.Sound(self._fp_effect_menu_select)
        self.brick_collide = pygame.mixer.Sound(self._fp_effect_brick_collide)
        self.paddle_collide = pygame.mixer.Sound(self._fp_effect_paddle_collide)


    def play_select(self):
        self.menu_select.play()


    def play_brick_collide(self):
        self.brick_collide.play()


    def play_paddle_collide(self):
        self.paddle_collide.play()


    def stop_music(self):
        pygame.mixer.stop()


    def volume_music(self, n):
        pygame.mixer.volume(n)


    def play_music_title(self):
        pygame.mixer.music.load(self._fp_music_title)
        pygame.mixer.music.play()


    def play_music_main(self):
        pygame.mixer.music.load(self._fp_music_main)
        pygame.mixer.music.play(-1)