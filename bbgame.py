import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BB Game")

BLACK = (0, 0, 0)
BALL_COLOR = (100, 100, 100)

ball_radius = 20
ball_x = WIDTH // 1
ball_y = HEIGHT // 6
ball_speed_x = 99
ball_speed_y = 8

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y *= -1

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
