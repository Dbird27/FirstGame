import pygame
import random
import time

#Setup Pygame
pygame.init()
width,height = 1320, 760
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
player_size = 20
player_speed = 60

grid_size = player_size*2
grid_color = "dark green"

apple_exists = False
apple_pos = pygame.Vector2(0,0)
apple_color = "red"

#For some logic later done, positing for up/right, negative for left/down
direction = 1
score = 0

#create a method to spawn apples
def spawnApple():
    global apple_pos, apple_exists
    x_pos = random.randint(0, width // 40)
    y_pos = random.randint(0, height // 40)
    apple_pos = pygame.Vector2(x_pos * 40 + 20, y_pos * 40 + 20)
    apple_exists = True

#Start the game logic here
while running:
    #poll for events
    #pygame.QUIT event means the user clicked the X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if player_pos == apple_pos:
        apple_exists = False
        score +=1
        print(score)

    if not apple_exists:
        spawnApple()

    #Fill screen with color to wipe away things from last frame
    screen.fill("forest green")

    for x in range(0, width, grid_size):
        pygame.draw.line(screen, grid_color, (x,0), (x,height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, grid_color, (0,y), (width, y))

    #Render game here
    pygame.draw.circle(screen, "salmon", player_pos, player_size)
    pygame.draw.circle(screen, apple_color, apple_pos, player_size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
        direction = -1
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
        direction = 1
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
        direction = -1
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt
        direction = 1

    #Force player to stay on screen
    if player_pos.x > width - player_size:
        player_pos.x = width - player_size
    if player_pos.x < player_size:
        player_pos.x = player_size
    if player_pos.y > height - player_size:
        player_pos.y = height - player_size
    if player_pos.y < player_size:
        player_pos.y = player_size
    
    #Force player to remain in center of square
    if player_pos.x % player_size != 0:
        player_pos.x = round(player_pos.x/player_size)*player_size
        if player_pos.x % grid_size == 0:
            player_pos.x += player_size * direction
    if player_pos.y % player_size != 0:
        player_pos.y = round(player_pos.y/player_size)*player_size
        if player_pos.y % grid_size == 0:
            player_pos.y += player_size * direction

    #flip() display to put work on screen
    pygame.display.flip()

    dt = clock.tick(60)/100 #Limits FPS to 60.

pygame.quit()