# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate robot's center position based on mouse position
    x = mouse_x - robot.get_width() / 2
    y = mouse_y - robot.get_height() / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
