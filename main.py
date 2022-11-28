# Import libraries and modules
import pygame
from pygame.locals import *
import constants


class Snake():
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.snake_body = pygame.image.load("images\snake_body.png")
        self.x = 100
        self.y = 100


    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)
        self.parent_window.blit(self.snake_body, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_rigth(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 100
        self.draw()





class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode()
        self.title = pygame.display.set_caption(constants.TITLE)
        self.window.fill(constants.BG_COLOR)
        icon = pygame.image.load("images\snake.png")
        pygame.display.set_icon(icon)

        self.snake = Snake(self.window)
        self.snake.draw()

        pygame.display.update()

    def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == KEYDOWN: 
                        if event.key == K_ESCAPE:
                            running = False

                        if event.key == K_ESCAPE:
                            self.snake.move_left()
                        
                        if event.key == K_RIGHT:
                            self.snake.move_rigth()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                    elif event.type == QUIT:
                        running = False

game = Game()
game.run()
