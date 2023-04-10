# WRITE YOUR SOLUTION HERE:
import pygame
import math
import time

pygame.init()
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

def draw_hand(angle, length, color, width=3):
    x_end = 320 + math.cos(angle) * length
    y_end = 240 - math.sin(angle) * length
    pygame.draw.line(window, color, (320, 240), (x_end, y_end), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 255, 255), (320, 240), 200, 3)

    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hour_angle = math.radians((hours % 12) * 30 - 90)
    minute_angle = math.radians(minutes * 6 - 90)
    second_angle = math.radians(seconds * 6 - 90)

    draw_hand(hour_angle, 100, (255, 0, 0), 6)
    draw_hand(minute_angle, 150, (0, 255, 0), 4)
    draw_hand(second_angle, 180, (0, 0, 255), 2)

    pygame.display.flip()
    clock.tick(30)
