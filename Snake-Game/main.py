import pygame
import sys
import random

WEIGHT = 720
HEIGHT = 720
FPS = 5

speed_x = 0
speed_y = 0

colors = {
    "light_green":(153, 255, 204),
    "light_yellow":(255, 255, 153),
    "light_red":(255, 102, 102),
    "light_blue":(153, 204, 255)
}

number_of_grids = 25

box_weight = WEIGHT/number_of_grids
box_height = HEIGHT/number_of_grids

pos_x = []
pos_y = []

for i in range(number_of_grids):
    pos_x.append(int((WEIGHT/number_of_grids)*i))
    pos_y.append(int((HEIGHT/number_of_grids)*i))

player_x = 12
player_y = 12

food_x = random.choice([i for i in range(19)])
food_y = random.choice([i for i in range(19)])

previos_pos = []
number_of_tail = 1
tail = []

def draw(screen):
    try:
        head = pygame.Rect((pos_x[player_x], pos_y[player_y], box_weight, box_height))
        food = pygame.Rect((pos_x[food_x], pos_y[food_y], box_weight, box_height))
    except:
        pygame.quit()
        sys.exit()

    pygame.draw.rect(screen, colors["light_red"], food)
    pygame.draw.rect(screen, colors["light_yellow"], head)

    if len(tail) != 0:
        for i,t in enumerate(tail):
            pygame.draw.rect(screen, colors["light_blue"], t)

            tail[i].x = pos_x[previos_pos[len(previos_pos)-(i+1)][0]]
            tail[i].y = pos_y[previos_pos[len(previos_pos)-(i+1)][1]]

    collision(head)

def collision(head):
    if player_x >= number_of_grids or player_y >= number_of_grids or player_x < 0 or player_y < 0:
        pygame.quit()
        sys.exit()
    
    for i in range(1, len(tail)):
        if tail[len(tail)-i].x == head.x or tail[len(tail)-i].y == head.y:
            pygame.quit()
            sys.exit()

pygame.init()
screen = pygame.display.set_mode((WEIGHT, HEIGHT))

clock = pygame.time.Clock()
runing = True

while runing:
    screen.fill(colors["light_green"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed_x, speed_y = 0, -1
            elif event.key == pygame.K_s:
                speed_x, speed_y = 0, 1
            elif event.key == pygame.K_a:
                speed_x, speed_y = -1, 0
            elif event.key == pygame.K_d:
                speed_x, speed_y = 1, 0
        
    player_x += speed_x
    player_y += speed_y

    if len(previos_pos) > number_of_tail:
        del previos_pos[0]
    
    previos_pos.append((player_x, player_y))

    if player_x == food_x and player_y == food_y:
        food_x = random.choice([i for i in range(19)])
        food_y = random.choice([i for i in range(19)])

        tail.append(pygame.Rect((pos_x[previos_pos[0][0]], pos_y[previos_pos[0][1]], box_weight, box_height)))
        number_of_tail += 1

    draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
