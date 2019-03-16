import pygame

from framework.scene import Scene
from framework.text import Text


class MenuScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        menu_rect = pygame.Rect(0, 0, 100, 30)

        menu_rect.center = director.screen.get_rect().center

        self.play = Text(
            menu_rect, 30, director.regular_text_color, director.screen, "PLAY")

    def mousebuttondown(self, button, position):
        if self.play.rect.collidepoint(position):
            self.director.set_scene("game")

    def update(self):
        position = pygame.mouse.get_pos()

        if self.play.rect.collidepoint(position):
            self.play.color = self.director.special_text_color
        else:
            self.play.color = self.director.regular_text_color

        self.play.prep_img()

    def render(self):
        super().render()

        self.play.render()
