import pygame

from core import settings
from core.abstract_artefact import AbstractArtefact


class AnimatedArtefact(AbstractArtefact):

    def __init__(self, image, pos_x=0, pos_y=0, frames=(1, 4)):
        super().__init__(image, pos_x, pos_y)
        self.sprite.image = pygame.image.load(image.format(1))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = pos_x
        self.sprite.rect[1] = pos_y
        self.tick = 0
        self.tick_limit = settings.FPS

        self.frames = (frames[0], frames[1] + 1)
        self.frame = 0
        self.images = [pygame.image.load(image.format(i)) for i in range(*self.frames)]

    def animate(self):
        self.tick += 1
        if self.tick >= self.tick_limit:
            self.tick = 0
            self.frame = self.frame + 1 if self.frame < self.frames[1] - 1 else self.frames[0]
        self.sprite.image = self.images[self.frame - 1]
        return self
