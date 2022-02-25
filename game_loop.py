from core.abstract_game_loop import AbstractGameLoop
from game import Game
from game_over import GameOver
from menu import Menu


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.menu = Menu()
        self.game = Game()
        self.game_over = GameOver()
        self.add_valid_key(*self.game.valid_keys)

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window).update()
        elif not self.game_over.change_scene:
            self.game_over.draw(self.window)
        else:
            self.restart()

    def restart(self):
        self.menu.change_scene = False
        self.game.change_scene = False
        self.game_over.change_scene = False
        self.game.restart()

    def check_keys(self, event):
        if not self.menu.change_scene:
            self.menu.check_keys(event)
        self.game.check_keys(event)
        if self.game.finished:
            self.game_over.check_keys(event)

    def check_events(self, event):
        self.game.check_events(event)
