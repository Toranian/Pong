import os, sys, time, random
import pygame
from settings import *

# Game display: 6 | Title: 7 | Game Exit: 8 | Initialization: 9-10
# Lead X & Y |
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
init = pygame.init()
print("{} Successes, {} Failures".format(init[0], init[1]))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 150)


# Message to screen.
def message_to_screen(msg, colour=(255, 255, 255)):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [WIDTH / 2, HEIGHT / 2])


# Random colour
def random_rgb_colour():
    global super_colour
    super_colour = (random.randint(0, 255), random.randint(0, 255,), random.randint(0, 255))


# Game loop
def game_loop():

    paddle_speed = 5
    speed = 4
    game_exit = False
    lead_x = WIDTH / 2
    lead_y = HEIGHT / 2

    ball_size = 15

    # Paddles
    paddle_1_x = 10
    paddle_1_y = (WIDTH / 2) - 150
    paddle_2_x = WIDTH - 20
    paddle_2_y = (WIDTH / 2) - 150
    paddle_size = [10, 100]

    lead_x_change = -speed
    lead_y_change = speed

    lead_paddle_x = 0
    lead_paddle_y = 0

    while not game_exit:
        # Event handler | Quit: 16 |
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    lead_paddle_y = -paddle_speed

                if event.key == pygame.K_s:
                    lead_paddle_y = paddle_speed

        # Bounce
        if lead_x <= paddle_1_x:
            lead_x_change = -speed

        # Game Over
        if lead_x >= WIDTH:
            lead_x_change = -speed
            # game_exit = True
        elif lead_x <= 0:
            lead_x_change = speed
            # game_exit = True
        if lead_y >= HEIGHT:
            lead_y_change = -speed
        elif lead_y <= 0:
            lead_y_change = speed

        lead_x += lead_x_change
        lead_y += lead_y_change
        paddle_1_y += lead_paddle_y

        gameDisplay.fill(BLACK)
        pygame.draw.rect(gameDisplay, WHITE, [lead_x, lead_y, ball_size, ball_size])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_1_x, paddle_1_y, paddle_size[0], paddle_size[1]])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_2_x, lead_y - 50, paddle_size[0], paddle_size[1]])
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
