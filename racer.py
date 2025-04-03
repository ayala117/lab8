import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

car_img = pygame.image.load("images/car.png")
car_img = pygame.transform.scale(car_img, (80, 100))
car_rect = car_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))

coin_img = pygame.image.load("images/coin.png")
coin_img = pygame.transform.scale(coin_img, (40, 40))

class Coin:
    def __init__(self):
        self.rect = coin_img.get_rect(center=(random.randint(50, WIDTH - 50), 0))
        self.value = random.choice([1, 2, 3])

    def draw(self):
        screen.blit(coin_img, self.rect)

coin = Coin()
obstacle_rect = pygame.Rect(random.randint(50, WIDTH - 50), 0, 60, 80)

score = 0
speed = 5
coin_speed = 3
obstacle_speed = 4
coin_count = 0
coins_needed_for_speedup = 5

running = True
while running:
    screen.fill(WHITE)
    screen.blit(car_img, car_rect)
    coin.draw()
    pygame.draw.rect(screen, RED, obstacle_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_rect.x -= speed
    if keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
        car_rect.x += speed

    coin.rect.y += coin_speed
    if coin.rect.top > HEIGHT:
        coin = Coin()

    if car_rect.colliderect(coin.rect):
        score += coin.value
        coin_count += 1
        print(f"Score: {score}")
        coin = Coin()

        if coin_count % coins_needed_for_speedup == 0:
            speed += 0.5
            coin_speed += 0.2
            obstacle_speed += 0.3

    obstacle_rect.y += obstacle_speed
    if obstacle_rect.top > HEIGHT:
        obstacle_rect.topleft = (random.randint(50, WIDTH - 50), 0)

    if car_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
