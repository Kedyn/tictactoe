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

        self.waiting_for_ai = False

    def keydown(self, key):
        if not self.waiting_for_ai:
            if key == pygame.K_1 and self.board.pieces[0] == PIECE.NONE:
                self.board.pieces[0] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_2 and self.board.pieces[1] == PIECE.NONE:
                self.board.pieces[1] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_3 and self.board.pieces[2] == PIECE.NONE:
                self.board.pieces[2] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_4 and self.board.pieces[3] == PIECE.NONE:
                self.board.pieces[3] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_5 and self.board.pieces[4] == PIECE.NONE:
                self.board.pieces[4] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_6 and self.board.pieces[5] == PIECE.NONE:
                self.board.pieces[5] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_7 and self.board.pieces[6] == PIECE.NONE:
                self.board.pieces[6] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_8 and self.board.pieces[7] == PIECE.NONE:
                self.board.pieces[7] = self.board.player_one.piece
                self.waiting_for_ai = True
            elif key == pygame.K_9 and self.board.pieces[8] == PIECE.NONE:
                self.board.pieces[8] = self.board.player_one.piece
                self.waiting_for_ai = True

    def update(self):
        if self.waiting_for_ai:
            # HERE GOES THE AI STUFF
            pass

    def render(self):
        super().render()

        self.board.render()
