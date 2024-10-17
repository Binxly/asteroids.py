from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            vector_1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector_2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            child_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_2 = Asteroid(self.position.x, self.position.y, new_radius)

            child_1.velocity = vector_1 * 1.2
            child_2.velocity = vector_2 * 1.2

        self.kill()
