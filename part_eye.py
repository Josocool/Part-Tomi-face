import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((480, 320))  #Size Display
pygame.display.set_caption("Eye")

BLUE = (0, 191, 255)
BLACK = (0, 0, 0)

# Function Draw eye
def draw_eye():
    screen.fill(BLACK)  # Background
    pygame.draw.circle(screen, BLUE, (240, 160), 80)  #  Circle
    pygame.display.flip()  # Update Display

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_eye()
