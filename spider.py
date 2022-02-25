from random import randrange

from core.animated_artefacts import AnimatedArtefact


class Spider(AnimatedArtefact):

    def __init__(self, pos_x=0, pos_y=0):
        super().__init__("assets/spider{}.png", pos_x, pos_y, (1, 4))
        self.tick_limit = 8


class SpiderFactory:

    @staticmethod
    def get_instance():
        return Spider(randrange(0, 300), -50)
