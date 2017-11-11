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
font = pygame.font.SysFont(None, 75)


# Message to screen.
def message_to_screen(msg, colour=(255, 255, 255)):
    screen_text = font.render(msg, True, colour)
    screen_text.get_rect()
    gameDisplay.blit(screen_text, [(WIDTH / 2), 0])


# Game loop
def game_loop():

    global speed, paddle_speed, score
    paddle_speed = 6
    speed = 4
    score = 0
    game_exit = False
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_size = 15

    # Paddles
    paddle_size = [10, 100]
    paddle_x = 20
    paddle_y = (WIDTH / 2) - 150
    paddle_2_x = WIDTH - (paddle_x * 2)
    paddle_2_y = ball_y - 50

    ball_x_change = random.choice([-speed, speed])
    ball_y_change = random.choice([-speed, speed])

    lead_paddle_y = 0

    def point():
        global speed, paddle_speed
        for i in range(0, 5):
            random_colour = (random.randint(0, 255), random.randint(0, 255,), random.randint(0, 255))
            ball = pygame.draw.rect(gameDisplay, random_colour, [ball_x, ball_y, ball_size, ball_size])
            pygame.display.update()
            time.sleep(0.1)
            speed += 0.01
            paddle_speed += 0.01

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

                if event.key == pygame.K_SPACE:
                    game_loop()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    lead_paddle_y = 0

                if event.key == pygame.K_s:
                    lead_paddle_y = 0
        # Paddle collision

        ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        paddle = pygame.Rect(paddle_x, paddle_y, paddle_size[0], paddle_size[1])
        paddle2 = pygame.Rect(paddle_2_x, ball_y - 50, paddle_size[0], paddle_size[1])

        if ball.colliderect(paddle):
            ball_x_change = speed
            speed += 0.1
            paddle_speed += 0.1
            score += 1

        if ball.colliderect(paddle2):
            ball_x_change = -speed
            speed += 0.1
            paddle_speed += 0.1
            score += 1
        # Point
        if ball_x > WIDTH:
            ball_x = WIDTH-20
            ball_x_change = -speed
            point()
            game_loop()
            
        elif ball_x < 0:
            ball_x = -speed
            ball_x_change = speed
            point()
            game_loop()

        # Wall bounce
        if ball_y >= HEIGHT:
            ball_y_change = -speed
        elif ball_y <= 0:
            ball_y_change = speed

        # Paddle Stop at Edges
        if paddle_x >= HEIGHT:
            lead_paddle_y = 0

        ball_x += ball_x_change
        ball_y += ball_y_change
        paddle_y += lead_paddle_y

        gameDisplay.fill(BLACK)
        message_to_screen(str(score))
        pygame.draw.rect(gameDisplay, WHITE, [ball_x, ball_y, ball_size, ball_size])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_x, paddle_y, paddle_size[0], paddle_size[1]])
        pygame.draw.rect(gameDisplay, WHITE, [paddle_2_x, ball_y - 50, paddle_size[0], paddle_size[1]])
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
