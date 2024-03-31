import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pickup Game')

# Cube properties
cube_size = 50
cube_x = screen_width // 2 - cube_size // 2
cube_y = screen_height // 2 - cube_size // 2
cube_speed = 5

# Object properties
object_size = 20
object_list = [{'x': random.randint(0, screen_width - object_size),
                'y': random.randint(0, screen_height - object_size)}]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the cube based on the pressed keys
    keys = pygame.key.get_pressed()
    cube_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * cube_speed
    cube_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * cube_speed

    # Keep the cube within the screen boundaries
    cube_x = max(0, min(cube_x, screen_width - cube_size))
    cube_y = max(0, min(cube_y, screen_height - cube_size))

    # Check for collisions with objects
    for obj in object_list:
        if cube_x < obj['x'] + object_size and \
           cube_x + cube_size > obj['x'] and \
           cube_y < obj['y'] + object_size and \
           cube_y + cube_size > obj['y']:
            # Collision detected, remove the object and increase the score
            object_list.remove(obj)
            score += 1
            # Add a new object at a random position
            object_list.append({'x': random.randint(0, screen_width - object_size),
                                'y': random.randint(0, screen_height - object_size)})

    # Fill the screen with white
    screen.fill(white)

    # Draw the cube
    pygame.draw.rect(screen, blue, (cube_x, cube_y, cube_size, cube_size))

    # Draw the objects
    for obj in object_list:
        pygame.draw.rect(screen, green, (obj['x'], obj['y'], object_size, object_size))

    # Display the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (screen_width - 150, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
