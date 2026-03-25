import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10
speed_increment = 5  # How much the speed increases per score

# Trail properties
trail_length = 15  # Number of trail segments
enemy_trail = []   # List to store previous positions

# Load images
player_image = pygame.image.load("player.jpg")
player_image = pygame.transform.scale(player_image, (player_size, player_size))

enemy_image = pygame.image.load("enemy.jpg")
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- BUG 1: Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Should move right

    # Prevent player from moving out of bounds
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- TRAIL LOGIC ---
    # Add current enemy position to the trail
    enemy_trail.append((enemy_pos[0], enemy_pos[1]))
    if len(enemy_trail) > trail_length:
        enemy_trail.pop(0)

    # --- BUG 2: Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        # The enemy should go back to the top with a new X position
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += speed_increment  # Increase enemy speed
        print(f"Score: {score}, Enemy Speed: {enemy_speed}")
        enemy_trail.clear()  # Clear trail when enemy resets

    # --- BUG 3: Collision Detection ---
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        game_over = True

    # Drawing
    screen.fill((0, 0, 0))

    # Draw enemy trail (fading effect)
    for i, (x, y) in enumerate(enemy_trail):
        alpha = int(255 * (i + 1) / trail_length)
        trail_surface = pygame.Surface((enemy_size, enemy_size), pygame.SRCALPHA)
        trail_surface.fill((255, 0, 0, alpha // 3))  # Fainter than main enemy
        screen.blit(trail_surface, (x, y))

    # Draw enemy image
    screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

    # Draw player image
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
