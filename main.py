import pygame
import sys
from game_logic import Game
from utils import *

def main():
    # Pygame Init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python Snake Game - Linked List Edition")
    
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24, bold=True)
    
    game = Game()
    
    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game.game_over and event.key == pygame.K_r:
                    game = Game() # Restart
                else:
                    game.handle_input(event)
        
        # Update
        game.update()
        
        # Draw
        game.draw(screen, font)
        
        # Render
        pygame.display.flip()
        
        # Frame Rate (Level arttıkça hızlanır)
        clock.tick(game.speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
