import pygame
from pynput.keyboard import Key, Listener
pygame.init()
from utils import load_sprite
from models import GameObject
from models import Spaceship

class Sdioretsa:
    def __init__(self):
        self.__init__
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.Spaceship = Spaceship((400,300))
        #self.asteroidone = GameObject((400,300), load_sprite("asteroidone"), (1,0))

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
            if Key == () == Key.right:
                self.spaceship.rotate(clockwise=True)
            elif Key == Key.left:
                self.spaceship.rotate(clockwise=False)

    def _process_game_logic(self):
        self.Spaceship.move()

    def _draw(self):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        pygame.display.flip()
        self.clock.tick(60)