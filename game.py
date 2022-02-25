import pygame

from bee import BeeFactory
from core.artefacts import Artefact
from flower import FlowerFactory
from spider import SpiderFactory
from text import Text


class Game:

    def __init__(self):
        self.bg1 = Artefact("assets/bg.png")
        self.bg2 = Artefact("assets/bg.png", 0, -640)
        self.spider = SpiderFactory.get_instance()
        self.flower = FlowerFactory.get_instance()
        self.bee = BeeFactory.get_instance()
        self.score = Text("0", 120, color=(255, 255, 255))
        self.power = Text("3", 60)
        self.score_caption = Text("Points", 40, color=(255, 120, 120))
        self.power_caption = Text("Power", 30, color=(255, 120, 120))
        self.valid_keys = [pygame.K_RETURN, pygame.K_SPACE]
        self.change_scene = False
        self.finished = False
        self.start_music()

    def start_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1)
        return self

    def draw(self, window):
        self.bg1.draw(window)
        self.bg2.draw(window)
        self.spider.draw(window)
        self.flower.draw(window)
        self.bee.draw(window)
        self.score.draw(window, 160, 50)
        self.power.draw(window, 50, 50)
        self.power_caption.draw(window, 30, 25)
        self.score_caption.draw(window, 140, 25)
        return self

    def check_events(self, event):
        self.bee.events(event)
        return self

    def check_keys(self, event):
        _ = event
        return self

    def update(self):
        self.animate_background()
        self.animate_spider()
        self.animate_flower()
        self.animate_bee()
        self.score.update(str(self.bee.points))
        self.power.update(str(self.bee.life))
        return self

    def animate_bee(self):
        self.bee.animate()
        self.check_collision()
        return self

    def check_collision(self):
        self.bee.check_collision(self.spider.group, "spider")
        self.bee.check_collision(self.flower.group, "flower")
        self.check_game_over()
        return self

    def check_game_over(self):
        if self.bee.life <= 0:
            self.finished = True
            self.change_scene = True

    def restart(self):
        self.finished = False
        self.bee.life = 3
        self.bee.points = 0

    def animate_background(self):
        self.bg1.sprite.rect[1] += 1
        self.bg2.sprite.rect[1] += 1

        if self.bg1.sprite.rect[1] >= 640:
            self.bg1.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640
        return self

    def animate_spider(self):
        self.spider.animate()
        self.spider.sprite.rect[1] += 10
        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = SpiderFactory.get_instance()
        return self

    def animate_flower(self):
        self.flower.animate()
        self.flower.sprite.rect[1] += 5
        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = FlowerFactory.get_instance()
        return self
