import pygame

from .piece import PIECE
from framework.text import Text


def pieceToString(piece):
    return "X" if piece is PIECE.X else "O" if piece is PIECE.O else " "


class Board:
    def __init__(self, director, rect, player_one, player_two):
        self.director = director
        self.rect = rect
        self.player_one = player_one
        self.player_two = player_two
        self.pieces = [PIECE.NONE for i in range(9)]
        self.winner = PIECE.NONE
        self.is_full = False

        text_height = int(rect.height * .1)
        text_rect = pygame.Rect(0, 0, rect.width / 2, text_height)

        self.player_one_text = Text(text_rect, text_height, director.regular_text_color,
                                    director.screen, player_one.name + " [" + pieceToString(player_one.piece) + "]")

        text_rect.top = text_rect.bottom

        self.player_one_score = Text(text_rect, text_height, director.regular_text_color,
                                     director.screen, str(player_one.score))

        text_rect.top = 0
        text_rect.left = text_rect.right

        self.player_two_text = Text(text_rect, text_height, director.regular_text_color,
                                    director.screen, player_two.name + " [" + pieceToString(player_two.piece) + "]")

        text_rect.top = text_rect.bottom

        self.player_two_score = Text(text_rect, text_height, director.regular_text_color,
                                     director.screen, str(player_two.score))

    def render(self):
        self.player_one_text.render()
        self.player_one_score.render()
        self.player_two_text.render()
        self.player_two_score.render()

        screen = self.director.screen

        y = self.player_one_score.rect.bottom + 2
        width = int(self.rect.width / 3)
        height = int((self.rect.height * .8) / 3)

        pygame.draw.line(screen, self.director.regular_text_color, (width, y),
                         (width, self.rect.height - 4))

        pygame.draw.line(screen, self.director.regular_text_color, (width * 2, y),
                         (width * 2, self.rect.height - 4))

        pygame.draw.line(screen, self.director.regular_text_color, (2, y + height),
                         (self.rect.width - 2, y + height))

        pygame.draw.line(screen, self.director.regular_text_color, (2, y + (height * 2)),
                         (self.rect.width - 2, y + (height * 2)))

    def reset(self):
        self.pieces.fill(PIECE.NONE)
        self.winner = PIECE.NONE
        self.is_full = False

    def copy(self, from_board):
        self.winner = from_board.winner
        self.is_full = from_board.is_full
        self.pieces = from_board.copy()

    def check(self):
        if self.pieces[0] == self.pieces[1] and self.pieces[1] == self.pieces[2]:
            self.winner = self.pieces[0]
        elif self.pieces[0] == self.pieces[3] and self.pieces[3] == self.pieces[6]:
            self.winner = self.pieces[0]
        elif self.pieces[0] == self.pieces[4] and self.pieces[4] == self.pieces[8]:
            self.winner = self.pieces[0]
        elif self.pieces[1] == self.pieces[4] and self.pieces[4] == self.pieces[7]:
            self.winner = self.pieces[1]
        elif self.pieces[2] == self.pieces[4] and self.pieces[4] == self.pieces[6]:
            self.winner = self.pieces[2]
        elif self.pieces[2] == self.pieces[5] and self.pieces[5] == self.pieces[8]:
            self.winner = self.pieces[2]
        elif self.pieces[3] == self.pieces[4] and self.pieces[4] == self.pieces[5]:
            self.winner = self.pieces[3]
        elif self.pieces[6] == self.pieces[7] and self.pieces[7] == self.pieces[8]:
            self.winner = self.pieces[6]

    def isFull(self):
        return all(object[tile] == PIECE.NONE for tile in self.pieces)

    def getEmptyIndexies(self):
        return [item for item, piece in self.pieces if piece == PIECE.NONE]

    def getBoardScoreForPiece(self, piece):
        if piece == self.winner:
            return 7
        elif PIECE.NONE == self.winner:
            return 0
        return -7
