import pygame

from core.animated_artefacts import AnimatedArtefact


class Bee(AnimatedArtefact):

    def __init__(self, pos_x, pos_y):
        super().__init__("assets/bee{}.png", pos_x, pos_y, (1, 4))
        pygame.mixer.init()
        self.sound_points = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_life = pygame.mixer.Sound("assets/sounds/spider_collide.ogg")
        self.tick_limit = 3
        self.life = 3
        self.points = 0

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30
            
    def check_collision(self, group, name):
        collision = pygame.sprite.spritecollide(self.sprite, group, True)
        if collision:
            if name == "flower":
                self.points += 1
                self.sound_points.play()
            if name == "spider":
                self.life -= 1
                self.sound_life.play()
        return self


class BeeFactory:

    @staticmethod
    def get_instance():
        return Bee(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
