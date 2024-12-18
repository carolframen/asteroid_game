import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
