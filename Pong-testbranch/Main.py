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

    global speed, paddle_speed
    paddle_speed = 6
    speed = 4
    game_exit = False
    ball_x = WIDTH / 2
    lead_y = HEIGHT / 2
    ball_size = 15

    # Paddles
    paddle_x = 10
    paddle_y = (WIDTH / 2) - 150
    paddle_2_x = WIDTH - 20
    paddle_2_y = (WIDTH / 2) - 150
    paddle_size = [10, 100]

    ball_x_change = -speed
    ball_y_change = speed

    lead_paddle_y = 0

    ball = pygame.draw.rect(gameDisplay, WHITE, [ball_x, lead_y, ball_size, ball_size])
    paddle = pygame.draw.rect(gameDisplay, WHITE, [paddle_x, paddle_y, paddle_size[0], paddle_size[1]])

    def point():
        global speed, paddle_speed
        for i in range(0, 5):
            random_colour = (random.randint(0, 255), random.randint(0, 255,), random.randint(0, 255))
            ball = pygame.draw.rect(gameDisplay, random_colour, [ball_x, lead_y, ball_size, ball_size])
            pygame.display.update()
            time.sleep(0.1)
            speed += 0.1
            paddle_speed += 0.1

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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    lead_paddle_y = 0

                if event.key == pygame.K_s:
                    lead_paddle_y = 0

        # Paddle collision

        if ball.colliderect(paddle):
            ball_x_change = -speed
            print('success')

        # Game Over
        if ball_x > WIDTH:
            ball_x = WIDTH-20
            ball_x_change = -speed
            point()
        elif ball_x < 0:
            ball_x = -speed
            ball_x_change = speed
            point()
        if lead_y >= HEIGHT:
            ball_y_change = -speed
        elif lead_y <= 0:
            ball_y_change = speed

        ball_x += ball_x_change
        lead_y += ball_y_change
        paddle_y += lead_paddle_y

        gameDisplay.fill(BLACK)
        pygame.draw.rect(gameDisplay, WHITE, [ball_x, lead_y, ball_size, ball_size])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_x, paddle_y, paddle_size[0], paddle_size[1]])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_2_x, lead_y - 50, paddle_size[0], paddle_size[1]])
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
