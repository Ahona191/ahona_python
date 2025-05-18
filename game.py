import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Apple")

clock = pygame.time.Clock()

# Load and scale images
apple_img = pygame.image.load("apple.jpg")
apple_img = pygame.transform.scale(apple_img, (40, 40))

basket_img = pygame.image.load("basket.jpeg")
basket_img = pygame.transform.scale(basket_img, (100, 50))

# Basket starts at center bottom
basket_x = WIDTH // 2 - 50
basket_y = HEIGHT - 60
basket_speed = 5

apple_x = random.randint(0, WIDTH - 40)
apple_y = 0
apple_speed = 3

score = 0
font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y, color=(255, 0, 0)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ← Basket movement →
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - 100:
        basket_x += basket_speed

    # Apple falling
    apple_y += apple_speed

    # Collision
    if basket_y < apple_y + 40 < basket_y + 50 and \
       basket_x < apple_x + 20 < basket_x + 100:
        score += 1
        apple_x = random.randint(0, WIDTH - 40)
        apple_y = -40

    # Missed apple = Game Over
    if apple_y > HEIGHT:
        draw_text("GAME OVER!!", WIDTH // 2 - 100, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Draw items
    screen.blit(apple_img, (apple_x, apple_y))
    screen.blit(basket_img, (basket_x, basket_y))
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()






