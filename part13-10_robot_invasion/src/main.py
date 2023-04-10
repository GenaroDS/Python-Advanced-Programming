# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

class FallingRobot:
    def __init__(self):
        self.x = random.randint(0, 640 - robot.get_width())
        self.y = -robot.get_height()
        self.velocity_y = random.randint(1, 4)
        self.velocity_x = random.choice([-1, 1]) * random.randint(1, 3)

    def update(self):
        self.y += self.velocity_y
        if self.y >= 480 - robot.get_height():
            self.y = 480 - robot.get_height()
            self.x += self.velocity_x

    def off_screen(self):
        return self.x + robot.get_width() < 0 or self.x > 640

    def draw(self):
        window.blit(robot, (self.x, self.y))

robots = []
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if random.random() < 0.05:
        robots.append(FallingRobot())

    for r in robots:
        r.update()
        r.draw()

    robots = [r for r in robots if not r.off_screen()]

    pygame.display.flip()
    clock.tick(60)
