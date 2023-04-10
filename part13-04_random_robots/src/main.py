# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

robot_width = robot.get_width()
robot_height = robot.get_height()

num_robots = 1000

for _ in range(num_robots):
    x_position = random.randint(0, 640 - robot_width)
    y_position = random.randint(0, 480 - robot_height)
    window.blit(robot, (x_position, y_position))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
