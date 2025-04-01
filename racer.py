
import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
RED = (255, 0, 0)


car_img = pygame.image.load("images/car.png")
car_img = pygame.transform.scale(car_img, (80, 100))  
car_rect = car_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))


coin_img = pygame.image.load("images/coin.png")
coin_img = pygame.transform.scale(coin_img, (40, 40))
coin_rect = coin_img.get_rect(center=(random.randint(50, WIDTH - 50), 0))


obstacle_rect = pygame.Rect(random.randint(50, WIDTH - 50), 0, 60, 80)


score = 0
speed = 5
coin_speed = 3
obstacle_speed = 4
running = True

while running:
    screen.fill(WHITE)  
    screen.blit(car_img, car_rect)  
    screen.blit(coin_img, coin_rect)  
    pygame.draw.rect(screen, RED, obstacle_rect)  
    
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_rect.x -= speed
    if keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
        car_rect.x += speed

    coin_rect.y += coin_speed
    if coin_rect.top > HEIGHT:
        coin_rect.topleft = (random.randint(50, WIDTH - 50), 0)

  
    if car_rect.colliderect(coin_rect):
        score += 1  
        print(f"Ұпай: {score}")
        coin_rect.topleft = (random.randint(50, WIDTH - 50), 0)  # Жаңа орын
        speed += 0.5 
        coin_speed += 0.2 
        obstacle_speed += 0.2 
    
    
    obstacle_rect.y += obstacle_speed
    if obstacle_rect.top > HEIGHT:
        obstacle_rect.topleft = (random.randint(50, WIDTH - 50), 0)

   
    if car_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False
    
   
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)  

pygame.quit()