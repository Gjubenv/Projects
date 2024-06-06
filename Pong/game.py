import pygame
import sys

pygame.init()

pygame.display.set_caption('Pong')

height = 480
width = 640
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

player1 = pygame.Rect(0, height/2 - 25, 10, 50)
player2 = pygame.Rect(width - 10, height/2 - 25, 10, 50)
ball = pygame.Rect(width/2 - 5, height/2 - 5, 10, 10)

ball_yspeed = 4
ball_xspeed = 4

player1_speed = 0
player2_speed = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -3
            if event.key == pygame.K_s:
                player1_speed = 3
            if event.key == pygame.K_UP:
                player2_speed = -3
            if event.key == pygame.K_DOWN:
                player2_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_speed = 0
            if event.key == pygame.K_s:
                player1_speed = 0
            if event.key == pygame.K_UP:
                player2_speed = 0
            if event.key == pygame.K_DOWN:
                player2_speed = 0

    # Collisions for ball
    ball.x += ball_xspeed
    ball.y += ball_yspeed
    if ball.bottom >= height or ball.top <= 0:
        ball_yspeed *= -1
    if ball.right >= width or ball.left <= 0:
        ball.x = width/2 - 5
        ball.y = height/2 - 5
        ball_xspeed *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_xspeed *= -1
    
    # Collisions for players
    player1.y += player1_speed
    player2.y += player2_speed
    if player1.bottom >= height and player1_speed > 0:
        player1_speed = 0
    if player1.top <= 0 and player1_speed < 0:
        player1_speed = 0
    if player2.bottom >= height and player2_speed > 0:
        player2_speed = 0
    if player2.top <= 0 and player2_speed < 0:
        player2_speed = 0
    
    screen.fill('black')
    pygame.draw.aaline(screen, 'white', (width/2, 0), (width/2, height))
    pygame.draw.rect(screen, 'white', player1)
    pygame.draw.rect(screen, 'white', player2)
    pygame.draw.rect(screen, 'white', ball)
    pygame.display.flip()
    clock.tick(60)