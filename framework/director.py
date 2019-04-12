import pygame
import sys

from twitch.main import *


class Director:
    def __init__(self, resolution, title):
        pygame.init()

        self.screen = pygame.display.set_mode(resolution)

        pygame.display.set_caption(title)

        self.scene_list = {}
        self.scene = None
        self.quit = False

        self.regular_text_color = (255, 255, 255)
        self.special_text_color = (0, 255, 255)

        self.previous_time = pygame.time.get_ticks()

        self.fps = 1000 / 60

    def loop(self):
        if self.scene is not None:

            twitch = connectToTwitch()

            while not self.quit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit = True

                getTwitchInput(twitch)

                if self.fps <= pygame.time.get_ticks() - \
                        self.previous_time:
                    self.scene.update()
                    self.scene.render()

                    self.previous_time = pygame.time.get_ticks()

                pygame.display.flip()

            if self.quit:
                for key, scene in self.scene_list.items():
                    if scene:
                        scene.exit()
                sys.exit()

    def set_scene(self, scene_name):
        self.scene = self.scene_list.get(scene_name)
        self.scene.reset()
