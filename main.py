import pygame as pg
import sys

import settings
from bird import *
from pipes import *
from game_objects import *
from settings import *
from text_display import *
from button import *

class FlappyBird:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.color = BIRD_COLOR
        self.load_assets()
        self.sound = Sound()
        self.score = Score(self)
        self.new_game()
        self.paused = False
        self.menu_state = "main"

    def load_assets(self):
        # ready message
        # load background
        self.pause_image = pg.image.load("assets/images/background_2.jpg").convert_alpha()
        self.pause_image = pg.transform.scale(self.pause_image, RES)
        # load button images
        self.start_img = pg.image.load("assets/buttons/start_button.png").convert_alpha()
        self.options_img = pg.image.load("assets/buttons/video_settings.png").convert_alpha()
        self.red_bird_img = pg.image.load("assets/bird/red1.png").convert_alpha
        self.blue_bird_img = pg.image.load("assets/bird/blue1.png").convert_alpha
        self.yellow_bird_img = pg.image.load("assets/bird/yellow1.png").convert_alpha
        self.green_pipe_img = pg.image.load("assets/images/green_pipe.png").convert_alpha()
        self.red_pipe_img = pg.image.load("assets/images/red_pipe.png").convert_alpha()
        self.sun_img = pg.image.load("assets/buttons/sun.png").convert_alpha()
        self.moon_img = pg.image.load("assets/buttons/moon.png").convert_alpha()
        self.back_img = pg.image.load("assets/buttons/back_button.png").convert_alpha()

        # bird
        self.bird_images = [pg.image.load(f"assets/bird/{self.color}{i}.png").convert_alpha() for i in range(3)]
        bird_image = self.bird_images[0]
        bird_size = bird_image.get_width() * BIRD_SCALE, bird_image.get_height() * BIRD_SCALE
        self.bird_images = [pg.transform.scale(sprite, bird_size) for sprite in self.bird_images]
        # background
        self.background_image = pg.image.load(f"assets/images/{DAY_TIME}.png").convert()
        self.background_image = pg.transform.scale(self.background_image, RES)
        # ground
        self.ground_image = pg.image.load("assets/images/base.png").convert()
        self.ground_image = pg.transform.scale(self.ground_image, (WIDTH, GROUND_HEIGHT))
        # pipes
        self.top_pipe_image = pg.image.load(f"assets/images/{PIPE_COLOR}pipe.png").convert_alpha()
        self.top_pipe_image = pg.transform.scale(self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_pipe_image = pg.transform.flip(self.top_pipe_image, False, True)
        # game_over



    def new_game(self):
        self.all_sprites_group = pg.sprite.Group()
        self.pipe_group = pg.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self, self.background_image)
        self.ground = Ground(self)
        self.pipe_handler = PipeHandler(self)

        self.paused_background = Background(self, self.pause_image)

        self.start_button = Button(self, 300, 300, self.start_img, 1)
        self.settings_button = Button(self, 1000, 300, self.options_img, 1)
        #self.red_bird_button = Button(self, 200, 200, self.red_bird_img, 2)
        #self.blue_bird_button = Button(self, 400, 200, self.blue_bird_img, 2)
        #self.yellow_bird_button = Button(self, 600, 200, self.yellow_bird_img, 2)
        self.sun_button = Button(self, 300, 600, self.sun_img, 0.1)
        self.moon_button = Button(self, 600, 600, self.moon_img, 0.1)
        self.red_pipe_button = Button(self, 300, 900, self.red_pipe_img, 10)
        self.green_pipe_button = Button(self, 600, 900, self.green_pipe_img, 10)
        self.back_button = Button(self, 0, 0, self.back_img, 1)

        self.pause_text = Text(self, "Press ESC to pause", WHITE, 0, 0, 40)
        self.choose_character_text = Text(self, "Press the bird you want!", BLACK, 400, 100, 40)
        self.choose_day_time_text = Text(self, "Press the moon for night mode and the sun for day mode!", BLACK, 400, 400, 40)
        self.choose_pipes_text = Text(self, "Press the pipes that you want to play with!", BLACK, 400, 700, 40)


    def draw(self):
        if self.paused:
            if self.menu_state == "main":
                self.paused_background.draw()
                if self.start_button.draw():
                    self.paused = False
                if self.settings_button.draw():
                    self.menu_state = "settings"  # Ska ha en meny där man kan ändra på settings
            if self.menu_state == "settings":
                self.screen.fill(WHITE)
                self.choose_character_text.draw()
                self.choose_day_time_text.draw()
                self.choose_pipes_text.draw()
                #if self.red_bird_button.draw():
                    #settings.BIRD_COLOR = "red"
                #if self.blue_bird_button.draw():
                    #settings.BIRD_COLOR = "blue"
                #if self.yellow_bird_button.draw():
                    #settings.BIRD_COLOR = "yellow"
                if self.sun_button.draw():
                    settings.DAY_TIME = "day"
                if self.moon_button.draw():
                    settings.DAY_TIME = "night"
                    print("night time!") # Måste gör om settings till class så att det går att ändra
                if self.red_pipe_button.draw():
                    settings.PIPE_COLOR = "red_"
                if self.green_pipe_button.draw():
                    settings.PIPE_COLOR = "green_"
                if self.back_button.draw():
                    self.menu_state = "main"
                # Ska kunna klicka på blå, röd eller gul fågel
                # Ska kunna klicka på dag eller natt-läge
                # Ska kunna klicka på red eller green pipes

        else:
            self.background.draw()
            self.all_sprites_group.draw(self.screen)
            self.ground.draw()
            self.score.draw()
            self.pause_text.draw()

        # pg.draw.rect(self.screen, "yellow", self.bird.rect, 4)
        # self.bird.mask.to_surface(self.screen, unsetcolor=None, dest=self.bird.rect, setcolor="green")
        pg.display.flip()

    def update(self):
        if self.paused:
            pass
        else:
            self.background.update()
            self.all_sprites_group.update()
            self.ground.update()
            self.pipe_handler.update()
            self.clock.tick(FPS)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.paused == False:
                        self.paused = True
                    else:
                        self.paused = False
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.bird.check_event(event)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = FlappyBird()
    game.run()