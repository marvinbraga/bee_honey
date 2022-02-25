import pygame

from core.artefacts import Artefact


class Menu:

    def __init__(self):
        self.background = Artefact("assets/start.png", 0, 0)
        self.change_scene = False

    def draw(self, window):
        self.background.draw(window)

    def check_keys(self, event):
        if event.key == pygame.K_RETURN:
            self.change_scene = True
