import pygame as pg
import pygame.mouse


class Button:
    def __init__(self, game, x, y, img, scale):
        self.game = game
        self.width = img.get_width()
        self.height = img.get_height()
        self.image = pg.transform.scale(img, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)
        self.clicked = False


    def draw(self):
        action = False
        #get mouse_pos
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            action = self.check_if_mouse_pressed(action)
            self.check_if_mouse_not_pressed()
        #draw button on screen
        self.game.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


    def check_if_mouse_pressed(self, action):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
            return action
        else:
            return action

    def check_if_mouse_not_pressed(self):
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

