import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Directional Shooting Game')

# Cube properties
cube_size = 50
cube_x = screen_width // 2 - cube_size // 2
cube_y = screen_height // 2 - cube_size // 2
cube_speed = 5

# Enemy properties
enemy_size = 30
enemy_speed = 1
enemies = [{'x': random.randint(0, screen_width - enemy_size),
            'y': random.randint(0, screen_height - enemy_size)}]

# Projectile properties
projectile_size = 10
projectiles = []
projectile_speed = 8

# Object properties
object_size = 20
object_list = [{'x': random.randint(0, screen_width - object_size),
                'y': random.randint(0, screen_height - object_size)}]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game state
game_over = False

# Player movement direction for shooting
last_movement = 'right'

# Explosion properties
explosion_active = False
explosion_max_size = 100
explosion_speed = 10
explosion_size = cube_size

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        # Update player movement based on keys and record the last direction moved
        movement_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * cube_speed
        movement_y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * cube_speed

        if movement_x > 0:
            last_movement = 'right'
        elif movement_x < 0:
            last_movement = 'left'
        elif movement_y > 0:
            last_movement = 'down'
        elif movement_y < 0:
            last_movement = 'up'

        cube_x += movement_x
        cube_y += movement_y

        # Keep the cube within the screen boundaries
        cube_x = max(0, min(cube_x, screen_width - cube_size))
        cube_y = max(0, min(cube_y, screen_height - cube_size))

        # Move enemies towards the player
        for enemy in enemies:
            angle = math.atan2(cube_y - enemy['y'], cube_x - enemy['x'])
            enemy['x'] += enemy_speed * math.cos(angle)
            enemy['y'] += enemy_speed * math.sin(angle)

            # Check for collision with the player
            if cube_x < enemy['x'] + enemy_size and \
               cube_x + cube_size > enemy['x'] and \
               cube_y < enemy['y'] + enemy_size and \
               cube_y + cube_size > enemy['y']:
                game_over = True  # Game over condition

        # Shooting mechanics
        if keys[pygame.K_SPACE]:
            # Determine shooting direction based on last movement
            if last_movement == 'right':
                angle = 0
            elif last_movement == 'left':
                angle = math.pi
            elif last_movement == 'up':
                angle = -math.pi / 2
            elif last_movement == 'down':
                angle = math.pi / 2

            projectiles.append({'x': cube_x + cube_size // 2 - projectile_size // 2,
                                'y': cube_y + cube_size // 2 - projectile_size // 2,
                                'angle': angle})

        # Move projectiles
        for projectile in projectiles:
            projectile['x'] += projectile_speed * math.cos(projectile['angle'])
            projectile['y'] += projectile_speed * math.sin(projectile['angle'])
        projectiles = [p for p in projectiles if 0 < p['x'] < screen_width and 0 < p['y'] < screen_height]

        # Updated collision handling
        to_remove_enemies = set()
        to_remove_projectiles = set()

        for enemy in enemies:
            for projectile in projectiles:
                if enemy['x'] < projectile['x'] + projectile_size and \
                   enemy['x'] + enemy_size > projectile['x'] and \
                   enemy['y'] < projectile['y'] + projectile_size and \
                   enemy['y'] + enemy_size > projectile['y']:
                    to_remove_enemies.add(tuple(enemy.items()))
                    to_remove_projectiles.add(tuple(projectile.items()))

        # Remove marked enemies and projectiles
        enemies = [e for e in enemies if tuple(e.items()) not in to_remove_enemies]
        projectiles = [p for p in projectiles if tuple(p.items()) not in to_remove_projectiles]

        # Explosion effect when the score reaches 15
        if score == 15 and not explosion_active:
            explosion_active = True
            explosion_size = cube_size

        if explosion_active:
            explosion_size += explosion_speed
            if explosion_size >= explosion_max_size:
                explosion_active = False
            explosion_x = cube_x - (explosion_size - cube_size) // 2
            explosion_y = cube_y - (explosion_size - cube_size) // 2
            pygame.draw.rect(screen, red, (explosion_x, explosion_y, explosion_size, explosion_size))
        else:
            # Draw the player cube
            pygame.draw.rect(screen, blue, (cube_x, cube_y, cube_size, cube_size))

        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, red, (enemy['x'], enemy['y'], enemy_size, enemy_size))

        # Draw projectiles
        for projectile in projectiles:
            pygame.draw.rect(screen, blue, (projectile['x'], projectile['y'], projectile_size, projectile_size))

        # Display the score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (650, 10))

    else:
        # Game over screen
        screen.fill(red)
        game_over_text = font.render("Game Over", True, white)
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
