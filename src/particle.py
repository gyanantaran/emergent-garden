"""
AUTHOR: Vishal Paudel
"""
from typing import Tuple, List
from ctypes import c_ubyte

import pygame
import random
import math

from src.constants import PARTICLE_DEFAULT_RADIUS, SCREEN_DIM, WALL_HEAT, WALL_BOUNDARY, PARTICLE_FORCE_LOWER_RANGE, PARTICLE_FORCE_UPPER_RANGE, PARTICLE_POWER_OF_DISTANCE, PARTICLE_DEFAULT_UPDATE_TIME, PARTICLE_LOSE_ENERGY

class Particle:
    def __init__(
        self, x: Tuple[int, int],
        v: Tuple[float, float],
        c: Tuple[c_ubyte, c_ubyte, c_ubyte],
        r: float = PARTICLE_DEFAULT_RADIUS
        ):
        """Initializes a particle

        Args:
            x   (Tuple[int, int]):      The postion     vector  of the particle
            v   (Tuple[float, float]):  The velocity    vector  of the particle
            c   (Tuple[int, int, int]): The color       RGB     of the particle
            r   (int):                  The radius      pixel   of the particle
        """
        # The position attributes
        self.x = x[0]
        self.y = x[1]

        # The velocity attributes
        self.vx = v[0]
        self.vy = v[1]

        # The look and feel attributes
        self.c = c
        self.r = r

        print("Particle initialised!")

    def update(self, dt: float):
        """Updates the attributes of the particle

        Args:
            dt (float): The delta time, time since the last frame update
        """
        # Updating the position attributes with the delta time
        # to keep it frame independent
        # apply_rule()
        pass

    def draw(self, screen: pygame.Surface):
        """Draws the particle(a circle)

        Args:
            screen (pygame.Surface):    The     screen  to draw onto
        """

        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r)


def apply_rule(particle_group1: List[Particle], particle_group2: List[Particle], g: float, dt: float = PARTICLE_DEFAULT_UPDATE_TIME):
    """Applies the force modifications to the particles of two particle groups

    Args:
        dt              (float):            The delta time
        particle_group1 (List[Particle]):   The first particle group on which modifications happen
        particle_group2 (List[Particle]):   The second particle group from which references the force modifications
        g               (float):            The force scale
    """

    for i in range(len(particle_group1)):
        a = particle_group1[i]
        for j in range(len(particle_group2)):
            b = particle_group2[j]

            fx = 0
            fy = 0

            dx = a.x - b.x
            dy = a.y - b.y

            d = (dx ** 2 + dy ** 2) ** (1 / 2)

            # THE RULE
            if (PARTICLE_FORCE_UPPER_RANGE > d > PARTICLE_FORCE_LOWER_RANGE):
                F = g * 1 / (d ** PARTICLE_POWER_OF_DISTANCE)# * len(particle_group1))

                fx = F * dx
                fy = F * dy
            else:
                if d < 0:
                    print("Invalid and Unexpected while applying rule")
                continue

            # ANOTHER MAIN RULE
            # LOSE ENERGY
            a.vx = (a.vx + fx * dt) * PARTICLE_LOSE_ENERGY
            a.vy = (a.vy + fy * dt) * PARTICLE_LOSE_ENERGY

            a.x += a.vx * dt
            a.y += a.vy * dt


            V = WALL_HEAT
            D = WALL_BOUNDARY
            # Boundary property
            if(a.x <= D):
                # a.x = SCREEN_DIM[0]

                a.x = D
                a.vx *= -V
            elif(a.x >= SCREEN_DIM[0] - D):
                # a.x = 0

                a.x = SCREEN_DIM[0] - D
                a.vx *= -V

            if(a.y <= D):
                # a.y = SCREEN_DIM[1]

                a.y = D
                a.vy *= -V
            elif(a.y >= SCREEN_DIM[1] - D):
                # a.y = 0

                a.y = SCREEN_DIM[1] - D
                a.vy *= -V


def instantiateGroup(
    num: int,
    c: tuple,
    frame: Tuple[Tuple[int, int], Tuple[int, int]]
    ) -> List[Particle]:
    """Method to instantiate a group of particles

    Args:
        num     (int):                                      The number          of particles in the group
        c       (tuple):                                    The color           of the group
        frame   (Tuple[Tuple[int, int], Tuple[int, int]]):  The cordinate frame for the group to spawn in

    Returns:
        group   List[Particle]:                             The list    of particles        in the group
    """
    random.seed()

    group = []
    for _ in range(num):
        x = random.randint(frame[0][0], frame[0][1])
        y = random.randint(frame[1][0], frame[1][1])

        # HARDCODE ALERT
        group.append(Particle(x=(x, y), v=(0.0, 0.0), c=c))

    return group
