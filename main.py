import pygame
import sys
from game_logic import Game
from utils import *

def main():
    """
    Entry point of the game to initialize Pygame and start the game loop.
    """
    # Initialize Pygame modules
    pygame.init()
    
    # Set up the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Team Bubble - Python Snake Game - Linked List Implementation")
    
    # Clock object to control the frame rate
    clock = pygame.time.Clock()
    
    # Font for rendering text
    font = pygame.font.SysFont("Arial", 24, bold=True)
    
    # Instantiate the Game logic class
    game = Game()
    
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if window close button is pressed
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check for restart command when game is over
                if game.game_over and event.key == pygame.K_r:
                    game = Game() # Reset game state
                else:
                    # Pass other potential inputs to game logic (movement)
                    game.handle_input(event)
        
        # --- Game Logic Update ---
        game.update()
        
        # --- Rendering / Drawing ---
        game.draw(screen, font)
        
        # Flip the display buffer to show new frame
        pygame.display.flip()
        
        # --- Frame Rate Control ---
        # Limits the game to 'game.speed' frames per second
        # As level increases, speed increases, making the loop run faster
        clock.tick(game.speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
