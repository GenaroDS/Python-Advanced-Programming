# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

robot_width = robot.get_width()
robot_height = robot.get_height()

offset = 10

for i in range(10):
    for j in range(10):
        x_position = j * (robot_width + offset)
        y_position = i * robot_height
        window.blit(robot, (x_position, y_position))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
