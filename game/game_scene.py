import pygame
import time
import random

from framework.scene import Scene
from framework.text import Text
from .piece import PIECE
from .player import Player
from .board import Board
from .ai import AI

from selflearning.tic_tac_toe import getHardStates, getEasyStates, makeMove


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        player_one = Player("TWITCH CHAT", PIECE.O)
        player_two = Player("AI", PIECE.X)

        self.board = Board(director, director.screen.get_rect(),
                           player_one, player_two)

        self.key_pressed = 0

        self.randValue = 0

        self.timeLeft = 3000

        self.waiting_for_ai = False

        self.ai = AI(player_two.piece)

        # self learning
        self.hard_states = getHardStates()
        self.easy_states = getEasyStates()
        self.states = self.hard_states

        self.game_type = "AI"

        self.flagState = 0
        self.isGameDone = False

        self.YELLOW = (255, 255, 0)
        self.WHITE = (255, 255, 255)

        # Display tie Text
        tie_rect = pygame.Rect(640, 100, 1, 1)
        # tie_rect.center = director.screen.get_rect().center
        self.tieText = Text(
            tie_rect, 50, (255, 255, 0), director.screen, "THE GAME IS A TIE!")

        # Display winner Text
        winner_rect = pygame.Rect(640, 100, 1, 1)
        winner_rect.center = director.screen.get_rect().center
        self.winnerText = Text(
            winner_rect, 50, (255, 255, 0), director.screen, "WE FOUND A WINNER!")

        # Display loser Text
        loser_rect = pygame.Rect(640, 100, 1, 1)
        self.loserText = Text(
            loser_rect, 50, (127, 0, 255), director.screen, "YOU LOST! I'M INEVITABLE!")

        # Audio files
        self.losing_sound = pygame.mixer.Sound("game/DreadedLost.ogg")
        self.winning_sound = pygame.mixer.Sound("game/DropOfBloodWon.ogg")

    def reset(self):
        self.board.reset()

        self.tieText.text = "THE GAME IS A TIE!"
        self.winnerText.text = "WE FOUND A WINNER!"
        self.loserText.text = "YOU LOST! I'M INEVITABLE!"

        self.key_pressed = 0

        if self.game_type == "AI":
            self.randValue = random.randint(1, 999)

            if self.randValue % 2 == 1:
                self.waiting_for_ai = False
                self.board.player_one_text.color = self.YELLOW
                self.board.player_two_text.color = self.WHITE

            else:
                self.waiting_for_ai = True
                self.board.player_one_text.color = self.WHITE
                self.board.player_two_text.color = self.YELLOW
        else:
            self.waiting_for_ai = True
            self.board.player_one_text.color = self.WHITE
            self.board.player_two_text.color = self.YELLOW

    def keydown(self, key):
        if not self.waiting_for_ai:
            self.key_pressed = key

            if key == pygame.K_m:
                self.director.set_scene("menu")

    def checkGameEnded(self):
        score = self.ai.getBoardScoreForPiece(self.board.pieces)

        if score == 7:
            self.losing_sound.play()
            self.flagState = 1
            self.isGameDone = True
            self.board.player_two.score += 1
            self.board.player_two_score.text = str(
                self.board.player_two.score)

            # pygame.time.delay(300)
            print("AI Won")
            print(self.board.player_two.score)

            return True
        elif score == -7:
            self.winning_sound.play()
            self.flagState = 2
            self.isGameDone = True
            self.board.player_one.score += 1
            self.board.player_one_score.text = str(
                self.board.player_one.score)
            # pygame.time.delay(300)
            print("Player Won")
            print(self.board.player_one.score)

            return True
        elif score == 0 and not self.ai.getEmptyIndexies(self.board.pieces):
            self.winning_sound.play()
            self.flagState = 0
            self.isGameDone = True
            # pygame.time.delay(300)
            print("TIE")

            return True

        return False

    def update(self):
        ticks = pygame.time.get_ticks()
        if not self.checkGameEnded():
            self.timeLeft = 3000
            if self.waiting_for_ai:
                if self.game_type == "AI":
                    self.board.pieces = self.ai.move(self.board.pieces)
                else:
                    game_state = [[self.board.pieces, []]]
                    results = makeMove(self.states, game_state)
                    self.board.pieces = results[0][-1][0]
                    # show confidence of move on results[1]
                    # the move is i-1 so u have to add 1
                    # is an array of moves and the confidence number
                    # check how to make the confidence number show only 2 decimals
                    # create an array of Text that will display if the game_type is not AI
                self.waiting_for_ai = False
                self.board.player_one_text.color = self.YELLOW
                self.board.player_two_text.color = self.WHITE
            elif self.key_pressed:
                if self.key_pressed == pygame.K_1 and self.board.pieces[0] == PIECE.NONE:
                    self.board.pieces[0] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_2 and self.board.pieces[1] == PIECE.NONE:
                    self.board.pieces[1] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_3 and self.board.pieces[2] == PIECE.NONE:
                    self.board.pieces[2] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_4 and self.board.pieces[3] == PIECE.NONE:
                    self.board.pieces[3] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_5 and self.board.pieces[4] == PIECE.NONE:
                    self.board.pieces[4] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_6 and self.board.pieces[5] == PIECE.NONE:
                    self.board.pieces[5] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_7 and self.board.pieces[6] == PIECE.NONE:
                    self.board.pieces[6] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_8 and self.board.pieces[7] == PIECE.NONE:
                    self.board.pieces[7] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
                elif self.key_pressed == pygame.K_9 and self.board.pieces[8] == PIECE.NONE:
                    self.board.pieces[8] = self.board.player_one.piece
                    self.waiting_for_ai = True
                    self.board.player_one_text.color = self.WHITE
                    self.board.player_two_text.color = self.YELLOW
        else:
            while self.timeLeft >= 0:
                self.timeLeft -= ticks
                if self.timeLeft < 0:
                    self.reset()

    def render(self):
        super().render()

        if self.isGameDone:
            if self.flagState == 1:
                self.loserText.prep_img()
                self.loserText.render()
                time.sleep(2)
                self.loserText.text = " "
                self.loserText.prep_img()
                self.loserText.render()
                #self.isGameDone = False
            elif self.flagState == 2:
                self.winnerText.prep_img()
                self.winnerText.render()
                time.sleep(2)
                self.winnerText.text = " "
                self.winnerText.prep_img()
                self.winnerText.render()
                #self.isGameDone = False
            else:
                self.tieText.prep_img()
                self.tieText.render()
                time.sleep(2)
                self.tieText.text = " "
                self.tieText.prep_img()
                self.tieText.render()
                #self.isGameDone = False

        self.board.render()
