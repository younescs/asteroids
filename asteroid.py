from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20,50)
        new_vector = self.velocity.rotate(rand)
        second_vector = self.velocity.rotate(-rand)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid1.velocity = new_vector*1.2
        small_asteroid2.velocity = second_vector*1.2
        

