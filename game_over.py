import pygame
from pygame.constants import K_RETURN

from core.artefacts import Artefact


class GameOver:

    def __init__(self):
        self.background = Artefact("assets/gameover.png", 0, 0)
        self.change_scene = False

    def draw(self, window):
        self.background.draw(window)

    def check_keys(self, event):
        key = pygame.key.get_pressed()
        if key[K_RETURN]:
            self.change_scene = True
