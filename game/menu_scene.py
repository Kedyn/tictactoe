import pygame

from framework.scene import Scene
from framework.text import Text


class MenuScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director, background)

        play_rect = pygame.Rect(600, 350, 100, 30)

        #menu_rect.center = director.screen.get_rect().center

        line2_rect = pygame.Rect(600, 400, 100, 30)

        #line2_rect.center = director.screen.get_rect().center

        line3_rect = pygame.Rect(600, 450, 100, 30)

        #line3_rect.center = director.screen.get_rect().center

        wait_rect = pygame.Rect(600, 200, 100, 30)

        self.wait = Text(
            wait_rect, 30, director.regular_text_color, director.screen, "WAITING FOR OPONENTS TO TYPE")

        self.play = Text(
            play_rect, 30, director.regular_text_color, director.screen, "!play ---> TO PLAY AGAINST MINIMAX AI")

        self.line2 = Text(
            line2_rect, 30, director.regular_text_color, director.screen, "!play easy  ---> TO PLAY AGAINST SELF LEARNING EASY AI")

        self.line3 = Text(
            line3_rect, 30, director.regular_text_color, director.screen, "!play hard  ---> TO PLAY AGAINST SELF LEARNING HARD AI")

    def keydown(self, key):
        if key == pygame.K_p:
            self.director.set_scene("game")
        elif key == pygame.K_e:
            game_scene = self.director.scene_list.get("game")

            game_scene.states = game_scene.easy_states
            game_scene.waiting_for_ai = True
            game_scene.game_type = "Self Learning"

            self.director.set_scene("game")
        elif key == pygame.K_h:
            game_scene = self.director.scene_list.get("game")

            game_scene.states = game_scene.hard_states
            game_scene.waiting_for_ai = True
            game_scene.game_type = "Self Learning"

            self.director.set_scene("game")

    def render(self):
        super().render()
        self.wait.render()
        self.play.render()
        self.line2.render()
        self.line3.render()
