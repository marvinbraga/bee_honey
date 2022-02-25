from abc import ABCMeta

import pygame


class AbstractArtefact(metaclass=ABCMeta):

    def __init__(self, image, pos_x=0, pos_y=0):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

    def draw(self, window):
        self.group.draw(window)
        return self
