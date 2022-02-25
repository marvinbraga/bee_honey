import pygame.font


class Text:

    def __init__(self, value: str, size=30, name="Montserrat Bold", color=(0, 0, 0)):
        self.color = color
        self.font = pygame.font.SysFont(name, size)
        self.render = self.font.render(value, True, color)

    def draw(self, window, x=0, y=0):
        window.blit(self.render, (x, y))

    def update(self, value):
        self.render = self.font.render(value, False, self.color)
        return self
