import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Gravity Sim")
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def update(self, other, G):
        dx = other.x - self.x
        dy = other.y - self.y
        r = (dx**2 + dy**2)**0.5
        if r == 0:
            return
        F = G * self.mass * other.mass / (r**2)
        self.vx += F * (dx / r) / self.mass
        self.vy += F * (dy / r) / self.mass
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen, color, radius):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)


sun = Particle(320, 240, 0, 0,500)
planet = Particle(320, 100, 1.8, 0, 10)

pygame.display.flip()
running = True
while running:
    screen.fill((20, 20, 20))

    G = 1
    planet.update(sun, G)

    sun.draw(screen, (252, 229, 112), 10)
    planet.draw(screen, (255, 255, 255), 5)
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
