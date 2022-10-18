import pygame as pg
import pygame.font

from settings import *


class Text:
    def __init__(self, game, text, text_col, x, y, font_size, font_type=None):
        self.game = game
        self.text = text
        self.font_size = font_size
        self.font = pg.font.SysFont(font_type, self.font_size)
        self.text_col = text_col
        self.x = x
        self.y = y
        self.img = self.font.render(self.text, True, self.text_col)


    def draw(self):
        self.game.screen.blit(self.img, (self.x, self.y))
