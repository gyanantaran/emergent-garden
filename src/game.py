"""
AUTHOR: Vishal Paudel
"""


import pygame

from src.constants import PARTICLE_DEFAULT_SPAWN_NUM, PARTICLE_COLOR_RED, PARTICLE_DEFAULT_SPAWN_FRAME, SCREEN_DIM, BACK_BLACK, PARTICLE_COLOR_YELLOW, PARTICLE_COLOR_GREEN, PARTICLE_COLOR_BLUE, FRAME_RATE
from src.particle import Particle, instantiateGroup, apply_rule

# HARDCODE
red_particles       = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM,  c=PARTICLE_COLOR_RED,       frame=PARTICLE_DEFAULT_SPAWN_FRAME)
yellow_particles  = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM,  c=PARTICLE_COLOR_YELLOW,    frame=PARTICLE_DEFAULT_SPAWN_FRAME)
green_particles   = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM,  c=PARTICLE_COLOR_GREEN,     frame=PARTICLE_DEFAULT_SPAWN_FRAME)
blue_particles   = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM,  c=PARTICLE_COLOR_BLUE,     frame=PARTICLE_DEFAULT_SPAWN_FRAME)

class Game:
    """This class represents the game instances
    """

    def __init__(self):
        """Generates a new Game object
        """
        pygame.init()
        self.game_running = True
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(size=SCREEN_DIM)

        self.dt = 0.1



    def run(self):
        """Runs the game
        """
        while self.game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            # for particle in self.particles:
            #     particle.update(self.dt)

            # INTERACTION DEFINITIONS
            apply_rule(red_particles, red_particles, -0.65)
            apply_rule(red_particles, yellow_particles, -0.1)
            apply_rule(red_particles, green_particles, -0.3)
            apply_rule(red_particles, blue_particles, 0.55)

            apply_rule(yellow_particles, yellow_particles, -0.6)
            apply_rule(yellow_particles, red_particles, 0.6)
            apply_rule(yellow_particles, green_particles, 0.4)
            apply_rule(yellow_particles, blue_particles, -0.3)

            apply_rule(green_particles, green_particles, 0.15)
            apply_rule(green_particles, red_particles, -0.4)
            apply_rule(green_particles, yellow_particles, 0.5)
            apply_rule(green_particles, blue_particles, -0.2)

            apply_rule(blue_particles, blue_particles, -0.5)
            apply_rule(blue_particles, red_particles, -0.4)
            apply_rule(blue_particles, yellow_particles, 0.5)
            apply_rule(blue_particles, green_particles, 0.5)

            self.screen.fill(BACK_BLACK)
            for i in range(len(red_particles)):
                red_particles[i].draw(self.screen)

            for i in range(len(yellow_particles)):
                yellow_particles[i].draw(self.screen)

            for i in range(len(green_particles)):
                green_particles[i].draw(self.screen)

            for i in range(len(blue_particles)):
                blue_particles[i].draw(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(FRAME_RATE) / 1000.0



    def quit(self):
        """Quits the game
        """
        pygame.quit()


