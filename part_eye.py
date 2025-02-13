import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((480, 320))  # Size Display
pygame.display.set_caption("Face")

# Colors
BLUE = (0, 191, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (135, 206, 250)

# Variables
eye_open = True

# Function to simulate mouth movement

def draw_mouth(speaking=False):
    if speaking:
        height = random.randint(10, 40)  # Random mouth height for wave effect
    else:
        height = 20  # Default mouth height
    pygame.draw.rect(screen, LIGHT_BLUE, (180, 250, 120, height))

# Function to draw face
def draw_face(speaking=False):
    screen.fill(BLACK)  # Background color
    eye_color = BLUE if eye_open else BLACK  # Eye blinking effect
    pygame.draw.circle(screen, eye_color, (160, 160), 80)  # Left eye
    pygame.draw.circle(screen, eye_color, (320, 160), 80)  # Right eye
    draw_mouth(speaking)
    pygame.display.flip()  # Update screen

# Main loop
last_blink = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Blink every 1 seconds
    if time.time() - last_blink > 0.5:
        eye_open = not eye_open
        last_blink = time.time()
    
    # Simulate speaking (randomized for demonstration)
    speaking = random.choice([True, False])
    
    draw_face(speaking)
    time.sleep(0.1)
