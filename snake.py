import pygame
import random


pygame.init()


WIDTH, HEIGHT = 1000,600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)


def generate_food():
    while True:
        new_food = (
            random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        )
        if new_food not in snake:  
            return new_food

food = generate_food()


score = 0
level = 1
speed = 7  
food_per_level = 3  

font = pygame.font.Font(None, 36)


def check_collision(head):
    return (
        head in snake or 
        head[0] < 0 or head[1] < 0 or 
        head[0] >= WIDTH or head[1] >= HEIGHT 
    )

running = True
while running:
    screen.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)

   
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

   
    if check_collision(new_head):
        running = False 
    snake.insert(0, new_head)  

    if new_head == food:
        score += 1
        food = generate_food()  
        
        if score % food_per_level == 0:
            level += 1
            speed += 1  
    else:
        snake.pop()  
   
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

   
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

   
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)  

pygame.quit()
