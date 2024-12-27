import pygame

#Setup Pygame
pygame.init()
width,height = 1320, 760
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
player_size = 20

grid_size = player_size*2
grid_color = "dark green"

#For some logic later done, positing for up/right, negative for left/down
direction = 1

#Start the game logic here
while running:
    #poll for events
    #pygame.QUIT event means the user clicked the X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill screen with color to wipe away things from last frame
    screen.fill("forest green")

    for x in range(0, width, grid_size):
        pygame.draw.line(screen, grid_color, (x,0), (x,height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, grid_color, (0,y), (width, y))

    #Render game here
    pygame.draw.circle(screen, "salmon", player_pos, player_size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 60 * dt
        direction = -1
    if keys[pygame.K_s]:
        player_pos.y += 60 * dt
        direction = 1
    if keys[pygame.K_a]:
        player_pos.x -= 60 * dt
        direction = -1
    if keys[pygame.K_d]:
        player_pos.x += 60 * dt
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
        if player_pos.y % grid_size ==0:
            player_pos.y += player_size * direction

    #flip() display to put work on screen
    pygame.display.flip()

    dt = clock.tick(60)/100 #Limits FPS to 60.

pygame.quit()