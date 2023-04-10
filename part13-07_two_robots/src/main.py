# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x1, y1 = 0, 0
x2, y2 = 0, 240
velocity1 = 1
velocity2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    x1 += velocity1
    if x1 + robot1.get_width() >= 640 or x1 <= 0:
        velocity1 = -velocity1

    x2 += velocity2
    if x2 + robot2.get_width() >= 640 or x2 <= 0:
        velocity2 = -velocity2

    clock.tick(60)
