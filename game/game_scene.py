import pygame

from framework.scene import Scene
from framework.text import Text
from .piece import PIECE
from .player import Player
from .board import Board


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        player_one = Player("TWITCH CHAT", PIECE.X)
        player_two = Player("AI", PIECE.O)

        self.board = Board(director, director.screen.get_rect(),
                           player_one, player_two)

    def mousebuttondown(self, button, position):
        super().mousebuttondown(button, position)

    def render(self):
        super().render()

        self.board.render()
