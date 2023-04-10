# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 320 - robot.get_width() // 2
y = 240 - robot.get_height() // 2
velocity = 3

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and y - velocity >= 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y + velocity <= 480 - robot.get_height():
        y += velocity
    if keys[pygame.K_LEFT] and x - velocity >= 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x + velocity <= 640 - robot.get_width():
        x += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
