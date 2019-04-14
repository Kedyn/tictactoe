import threading

from game.main import Game
from twitch.main import *

playing = True

game = Game()


def startGame():
    game.play()


def connectToChat():
    connectToTwitch(game)


if __name__ == "__main__":
    threading.Thread(target=startGame).start()
    threading.Thread(target=connectToChat).start()
