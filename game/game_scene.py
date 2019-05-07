import pygame
import time

from framework.scene import Scene
from framework.text import Text
from .piece import PIECE
from .player import Player
from .board import Board
from .ai import AI


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        player_one = Player("TWITCH CHAT", PIECE.X)
        player_two = Player("AI", PIECE.O)

        self.board = Board(director, director.screen.get_rect(),
                           player_one, player_two)

        self.key_pressed = 0

        self.waiting_for_ai = False

        self.ai = AI(player_two.piece)

    def reset(self):
        self.board.reset()

        self.key_pressed = 0

        self.waiting_for_ai = False

    def keydown(self, key):
        if not self.waiting_for_ai:
            self.key_pressed = key

    def checkGameEnded(self):
        score = self.ai.getBoardScoreForPiece(self.board.pieces)

        if score == 7:
            self.board.player_two.score += 1
            time.sleep(3)
            return True
        elif score == -7:
            self.board.player_one.score += 1
            time.sleep(3)
            return True
        elif score == 0 and not self.ai.getEmptyIndexies(self.board.pieces):
            time.sleep(3)
            return True

        return False

    def update(self):
        if not self.checkGameEnded():
            if self.waiting_for_ai:
                self.board.pieces = self.ai.move(self.board.pieces)
                self.waiting_for_ai = False
            elif self.key_pressed:
                if self.key_pressed == pygame.K_1 and self.board.pieces[0] == PIECE.NONE:
                    self.board.pieces[0] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_2 and self.board.pieces[1] == PIECE.NONE:
                    self.board.pieces[1] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_3 and self.board.pieces[2] == PIECE.NONE:
                    self.board.pieces[2] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_4 and self.board.pieces[3] == PIECE.NONE:
                    self.board.pieces[3] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_5 and self.board.pieces[4] == PIECE.NONE:
                    self.board.pieces[4] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_6 and self.board.pieces[5] == PIECE.NONE:
                    self.board.pieces[5] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_7 and self.board.pieces[6] == PIECE.NONE:
                    self.board.pieces[6] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_8 and self.board.pieces[7] == PIECE.NONE:
                    self.board.pieces[7] = self.board.player_one.piece
                    self.waiting_for_ai = True
                elif self.key_pressed == pygame.K_9 and self.board.pieces[8] == PIECE.NONE:
                    self.board.pieces[8] = self.board.player_one.piece
                    self.waiting_for_ai = True
        else:
            self.reset()

    def render(self):
        super().render()

        self.board.render()
