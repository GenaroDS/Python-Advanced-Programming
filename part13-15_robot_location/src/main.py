# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

def random_position():
    x = random.randint(0, 640 - robot.get_width())
    y = random.randint(0, 480 - robot.get_height())
    return x, y

x, y = random_position()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if x <= mouse_x <= x + robot.get_width() and y <= mouse_y <= y + robot.get_height():
                x, y = random_position()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
