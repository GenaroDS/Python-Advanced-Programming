# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_image = pygame.image.load("robot.png")
num_robots = 10
robots = [{"angle": 2 * math.pi * i / num_robots, "x": 0, "y": 0} for i in range(num_robots)]

radius = 100
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for robot in robots:
        robot["angle"] += 0.01
        robot["x"] = 320 + math.cos(robot["angle"]) * radius - robot_image.get_width() / 2
        robot["y"] = 240 + math.sin(robot["angle"]) * radius - robot_image.get_height() / 2
        window.blit(robot_image, (robot["x"], robot["y"]))

    pygame.display.flip()
    clock.tick(60)
