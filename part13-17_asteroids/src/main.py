import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def random_position():
    x = random.randint(0, 640 - rock.get_width())
    return x

robot_x = 320 - robot.get_width() // 2
rock_x = random_position()
rock_y = 0

points = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= 5
    if keys[pygame.K_RIGHT]:
        robot_x += 5

    robot_x = max(0, min(640 - robot.get_width(), robot_x))

    rock_y += 5
    if rock_y + rock.get_height() > 480:
        if robot_x <= rock_x <= robot_x + robot.get_width() or robot_x <= rock_x + rock.get_width() <= robot_x + robot.get_width():
            points += 1
            rock_x = random_position()
            rock_y = 0
        else:
            break

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, 0))
    window.blit(rock, (rock_x, rock_y))

    score_text = font.render(f"Points: {points}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
