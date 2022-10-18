import pygame as pg
from settings import *


class Score:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.Font(None, 150)
        self.font_pos = (WIDTH // 2, HEIGHT // 8)

    def draw(self):
        score = self.game.pipe_handler.passed_pipes
        self.text = self.font.render(f"{score}", True, "white")
        self.game.screen.blit(self.text, self.font_pos)

class Sound:
    def __init__(self):
        self.hit_sound = pg.mixer.Sound("assets/sound/hit.wav")
        self.point_sound = pg.mixer.Sound("assets/sound/point.wav")
        self.wing_sound = pg.mixer.Sound("assets/sound/wing.wav")

class Background:
    def __init__(self, game, image):
        self.game = game
        self.x = 0
        self.y = 0
        self.speed = SCROLL_SPEED - 2
        self.image = image


    def update(self):
        self.x = (self.x - self.speed) % -WIDTH

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
        self.game.screen.blit(self.image, (WIDTH + self.x, self.y))



class Ground(Background):
    def __init__(self, game):
        self.game = game
        super().__init__(game, self.game.ground_image)
        self.y = GROUND_Y
        self.speed = SCROLL_SPEED
