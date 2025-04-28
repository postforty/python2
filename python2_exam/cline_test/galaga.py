import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 20
player_speed = 50

# Enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(50, 150)
enemy_speed = 0.1

# Player bullet
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"  # ready - can fire, fire - is traveling

# Score
score = 0
font = pygame.font.Font(None, 36)


def player(x, y):
    pygame.draw.rect(screen, white, (x, y, player_width, player_height))


def enemy(x, y):
    pygame.draw.rect(screen, yellow, (x, y, enemy_width, enemy_height))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, white, (x + player_width // 2 -
                     bullet_width // 2, y, bullet_width, bullet_height))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < enemy_width / 2 + bullet_width / 2:
        return True
    else:
        return False


# Game loop
running = True
while running:
    screen.fill(black)

    # Player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed

    # Keep player within screen bounds
    player_x = max(0, player_x)
    player_x = min(player_x, screen_width - player_width)

    # Enemy movement
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= screen_width - enemy_width:
        enemy_speed *= -1
        enemy_y += 10

    # Bullet movement
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        fire_bullet(bullet_x, bullet_y)
        if bullet_y < 0:
            bullet_state = "ready"
            bullet_y = player_y

    # Collision detection
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        score += 1
        bullet_state = "ready"
        bullet_y = player_y
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(50, 150)

    # Score rendering
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()

pygame.quit()
