# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x1, y1 = 200, 240
x2, y2 = 440, 240
velocity = 3

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_UP] and y1 - velocity >= 0:
        y1 -= velocity
    if keys[pygame.K_DOWN] and y1 + velocity <= 480 - robot1.get_height():
        y1 += velocity
    if keys[pygame.K_LEFT] and x1 - velocity >= 0:
        x1 -= velocity
    if keys[pygame.K_RIGHT] and x1 + velocity <= 640 - robot1.get_width():
        x1 += velocity

    # Player 2 movement
    if keys[pygame.K_w] and y2 - velocity >= 0:
        y2 -= velocity
    if keys[pygame.K_s] and y2 + velocity <= 480 - robot2.get_height():
        y2 += velocity
    if keys[pygame.K_a] and x2 - velocity >= 0:
        x2 -= velocity
    if keys[pygame.K_d] and x2 + velocity <= 640 - robot2.get_width():
        x2 += velocity

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()
    clock.tick(60)
