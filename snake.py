import pygame
import time
import sys
import random

pygame.init()
screen = pygame.display.set_mode((500,500))

def draw_rectangle(surf, x, y, color):
    pygame.draw.rect(surf, color, (x*5,y*5,4,4))

for x in range(100):
    for y in range(100):
        draw_rectangle(screen, x, y, (128,128,128))

snake_x = 50
snake_y = 50
pygame.display.flip()

clock = pygame.time.Clock()

starting_length = 5
starting_food_length = 10

foods = []
for i in range(starting_food_length):
    foods.append((random.randint(0,99), random.randint(0,99)))

snake_x_diff = 0
snake_y_diff = -1
snake_chain = [(snake_x, snake_y)]
for i in range(1, 5):
    snake_chain.append((snake_x, snake_y+i))
    draw_rectangle(screen, snake_x, snake_y+1, (0,128,0))
lost = False
while True:
    clock.tick(10)
    events = pygame.event.get()
    for food in foods:
        draw_rectangle(screen, food[0], food[1], (128,0,0))
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_y_diff == 0:
                snake_x_diff = 0
                snake_y_diff = -1
            elif event.key == pygame.K_DOWN and snake_y_diff == 0:
                snake_x_diff = 0
                snake_y_diff = 1
            elif event.key == pygame.K_LEFT and snake_x_diff == 0:
                snake_x_diff = -1
                snake_y_diff = 0
            elif event.key == pygame.K_RIGHT and snake_x_diff == 0:
                snake_x_diff = 1
                snake_y_diff = 0
    if not lost:
        if snake_x == 0:
            if snake_x_diff == -1:
                lost = True
        if snake_x == 99:
            if snake_x_diff == 1:
                lost = True
        snake_x += snake_x_diff
        if snake_y == 0:
            if snake_y_diff == -1:
                lost = True
        if snake_y == 99:
            if snake_y_diff == 1:
                lost = True
        snake_y += snake_y_diff

        if (snake_x, snake_y) in snake_chain:
            lost = True
        last_link = snake_chain.pop()
        if (snake_x, snake_y) in foods:
            food_idx = foods.index((snake_x, snake_y))
            if food_idx > -1:
                snake_chain.append(last_link)
                foods.pop(food_idx)
                foods.append((random.randint(0,99), random.randint(0,99)))
        snake_chain = [(snake_x, snake_y)] + snake_chain
        draw_rectangle(screen, snake_chain[0][0], snake_chain[0][1], (0,128,0))
        if snake_x_diff != 0 or snake_y_diff != 0:
            draw_rectangle(screen, last_link[0], last_link[1], (128,128,128))
    else:
        for x in range(100):
            for y in range(100):
                draw_rectangle(screen, x, y, (128,0,0))

    pygame.display.flip()
    pygame.event.clear()
