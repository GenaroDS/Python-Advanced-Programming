# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

robot_width = robot.get_width()

for i in range(10):
    window.blit(robot, (i * robot_width, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
