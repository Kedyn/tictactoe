from .settings import *
import socket
import re
import pyautogui


def connectToTwitch():
    twitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    twitch.connect((HOST, PORT))
    twitch.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    twitch.send("NICK {}\r\n".format(NICK).encode("utf-8"))

    connected = True

    while connected:
        chat = twitch.recv(4096).decode("utf-8")

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
                if line == "":
                    continue
                else:
                    tokens = line.split(":", 2)
                    user = tokens[1].split("!", 1)[0]

                    try:
                        msg = tokens[2]
                    except:
                        msg = ""

                    if user in OWNER:
                        if msg == "!quit":
                            connected = False
                            pyautogui.keyDown('esc')
                print(line)
                pass

    twitch.close()
