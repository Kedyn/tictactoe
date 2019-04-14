import threading

from game.main import Game
from twitch.main import *

playing = True

game = Game()


def startGame():
    game.play()

    playing = False


def connectToChat():
    connectToTwitch(playing)


if __name__ == "__main__":
    threading.Thread(target=startGame).start()
    threading.Thread(target=connectToChat).start()
