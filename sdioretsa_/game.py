import pygame
pygame.init()
from utils import load_sprite
from models import GameObject

class Sdioretsa:
    def __init__(self):
        self.__init__
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.spaceship = GameObject((400,300), load_sprite("spaceship"), (0,0))
        self.asteroidone = GameObject((400,300), load_sprite("asteroidone"), (1,0))

    def main_loop(self):
        run = True
        
        while run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self._process_game_logic()
            self._draw()

    def _init_pygame_(self):
        pygame.init()
        pygame.display.set_caption("Sdioretsa")
    
    def _handle_input(self):
        pass

    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroidone.move()

    def _draw(self):
        self.screen.fill((0,0,0))
        self.spaceship.draw(self.screen)
        self.asteroidone.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)