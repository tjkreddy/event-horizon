import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Gravity Sim")


class Particle:
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def update(self, other, G):
         # gravity calculation between self and other goes here

    def draw(self, screen, color, radius):
        # draw circle goes here


sun = Particle(320, 240, 0, 0,500)
planet = Particle(320, 100, 1.8, 0, 10)

pygame.display.flip()
running = True
while running:
    screen.fill((20, 20, 20))
    
    G = 1
    r = ((sun.x - planet.x)**2 + (sun.y - planet.y)**2)**0.5
    F = G * sun.mass * planet.mass / (r**2)

    dx = sun.x - planet.x
    dy = sun.y - planet.y
    Fx = F * (dx/r)
    Fy = F * (dy/r)

    planet.vx += Fx/planet.mass
    planet.vy += Fy/planet.mass

    planet.x += planet.vx
    planet.y += planet.vy

    pygame.draw.circle(screen, (252, 229, 112), (int(sun.x), int(sun.y)), 10) 
    pygame.draw.circle(screen, (255, 255, 255), (int(planet.x), int(planet.y)), 5)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
