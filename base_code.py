import pygame
import random
import copy
import time

#Setup Pygame
pygame.init()
width,height = 1320, 760
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
dt = 0
move_speed = 4

player_move = False
player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)
player_size = 20
player_character = [player_pos]
snake_head = player_pos
player_loss = False

loss_screen = pygame.Rect(0,0,screen.get_width(),screen.get_height())

grid_size = player_size*2
grid_color = "dark green"

apple_exists = False
apple_pos = pygame.Vector2(0,0)
apple_color = "red"

#For some logic later down, positing for up/right, negative for left/down
direction =""
score = 0
wait_count = 0

#create a method to spawn apples
def spawnApple():
    global apple_pos, apple_exists
    x_pos = random.randint(0, (width-40) // 40)
    y_pos = random.randint(0, (height-40) // 40)
    apple_pos = pygame.Vector2(x_pos * 40 + 20, y_pos * 40 + 20)
    apple_exists = True

#Start the game logic here
while running:
    #poll for events
    #pygame.QUIT event means the user clicked the X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if snake_head == apple_pos:
        apple_exists = False
        score +=1
        print(score)
    elif player_move:
        player_character.pop()
        player_move = False

    if not apple_exists:
        spawnApple()

    #Handle player pressing key
    keys = pygame.key.get_pressed()
    new_head = copy.copy(snake_head)
    if keys[pygame.K_w]:
        new_head.y -= grid_size
        direction = "up"
        player_move=True
    elif keys[pygame.K_s]:
        new_head.y += grid_size
        direction = "down"
        player_move=True
    elif keys[pygame.K_a]:
        new_head.x -= grid_size
        direction = "left"
        player_move=True
    elif keys[pygame.K_d]:
        new_head.x += grid_size
        direction = "right"
        player_move=True
    else:
        wait_count+=1

    #Handle snake moving on it's own
    if wait_count == move_speed:
        wait_count = 0
        player_move=True
        if direction == "up":
            new_head.y -= grid_size
        elif direction == "down":
            new_head.y += grid_size
        elif direction == "left":
            new_head.x -= grid_size
        else:
            new_head.x += grid_size
    

    #Update player character
    if player_move:
        player_character.insert(0,new_head)
        snake_head = player_character[0]


    #Force player to stay on screen, also first lose condition
    if snake_head.x > width - player_size:
        snake_head.x = width - player_size
        player_loss = True
    if snake_head.x < player_size:
        snake_head.x = player_size
        player_loss = True
    if snake_head.y > height - player_size:
        snake_head.y = height - player_size
        player_loss = True
    if snake_head.y < player_size:
        snake_head.y = player_size
        player_loss = True
    #Handle player loss:    

    #Fill screen with color to wipe away things from last frame
    screen.fill("forest green")
    #Draw the grid
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, grid_color, (x,0), (x,height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, grid_color, (0,y), (width, y))

    #Render game here, aswell as Set second condition for player loss, hitting themselves
    for index,part in enumerate(player_character):
        pygame.draw.circle(screen, "salmon", part, player_size)
        if (part.x == snake_head.x) and (part.y == snake_head.y) and index>1:
            player_loss = True
    pygame.draw.circle(screen, apple_color, apple_pos, player_size)

    if player_loss:
        pygame.draw.ellipse(screen, "red", loss_screen,0)
        running = False
    #flip() display to put work on screen
    pygame.display.flip()

    clock.tick(10) #Limits FPS to 60.

pygame.quit()