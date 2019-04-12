from .settings import *
import socket
import re

def connectToTwitch():
    twitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    twitch.connect((HOST, PORT))
    twitch.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    twitch.send("NICK {}\r\n".format(NICK).encode("utf-8"))

    return twitch


def getTwitchInput(twitch):
    try:
        chat = twitch.recv(4096).decode("utf-8")
    except socket.error:
        print("Twitch connection error")
    except:
        print("Twitch unknown error")
    else:
        for line in chat.split("\n"):
            line = line.strip("\r\n")

            if line == "PING :tmi.twitch.tv":
                twitch.send("PONG :tmi.twitch.tv".encode("utf-8"))
            elif line == ":tmi.twitch.tv 376 {} :>".format(NICK):
                print("Connection to twitch successful... joining bot channel...")
                twitch.send("JOIN #{}\r\n".format(CHAN).encode("utf-8"))
            elif line == ":{}.tmi.twitch.tv 366 {} #{} :End of /NAMES list".format(NICK, NICK, NICK):
                print("Joined bot channel... ready to take commands...")
            else:
                pass
