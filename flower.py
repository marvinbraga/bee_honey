from random import randrange

from core.animated_artefacts import AnimatedArtefact


class Flower(AnimatedArtefact):

    def __init__(self, pos_x=0, pos_y=0):
        super().__init__("assets/flower{}.png", pos_x, pos_y, (1, 2))
        self.tick_limit = randrange(4, 17)


class FlowerFactory:

    @staticmethod
    def get_instance():
        return Flower(randrange(0, 300), -50)
