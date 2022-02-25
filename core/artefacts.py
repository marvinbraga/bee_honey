import pygame

from core.abstract_artefact import AbstractArtefact
from core.animated_artefacts import AnimatedArtefact


class Artefact(AbstractArtefact):

    def __init__(self, image, pos_x=0, pos_y=0):
        super().__init__(image, pos_x, pos_y)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y
