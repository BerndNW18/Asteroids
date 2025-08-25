from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        deviation = random.uniform(20, 50)
        _new_velos = [self.velocity.rotate(deviation), self.velocity.rotate(-deviation)]
        new_velos = [v * 1.2 for v in _new_velos]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for v in new_velos:
            a = Asteroid(self.position.x, self.position.y, new_radius)
            a.velocity = v