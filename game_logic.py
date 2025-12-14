import random
import json
import os
import pygame
from snake_ll import SnakeLinkedList
from utils import *

class Game:
    """
    Main Game Controller class.
    Manages the game state, including the snake, food, score, and game loop events.
    """
    def __init__(self):
        self.snake = SnakeLinkedList()
        self.food = None
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED
        self.game_over = False
        self.high_score = self.load_high_score()
        
        # Spawn the first food item
        self.spawn_food()

    def spawn_food(self):
        """
        Generates a new food item at a random position on the grid.
        Ensures that the food does not spawn on the snake's body.
        """
        while True:
            # Generate random coordinates within grid bounds
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # Check if the generated position is currently occupied by the snake
            on_snake = False
            current = self.snake.head
            while current is not None:
                if current.x == x and current.y == y:
                    on_snake = True
                    break
                current = current.next
            
            # If valid position found, place food and exit loop
            if not on_snake:
                self.food = (x, y)
                break

    def handle_input(self, event):
        """
        Processes keyboard input to change the snake's direction.
        
        Prevents 180-degree turns (e.g., trying to go DOWN while moving UP),
        as this would cause an immediate death/collision.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.snake.direction != DOWN:
                self.snake.direction = UP
            elif event.key == pygame.K_DOWN and self.snake.direction != UP:
                self.snake.direction = DOWN
            elif event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                self.snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                self.snake.direction = RIGHT

    def update(self):
        """
        Updates the game state for the current frame.
        Handles movement, collision checks, and game over logic.
        """
        if self.game_over:
            return

        # Move the snake based on current direction
        self.snake.move()
        
        # Check for collisions with walls or self
        self.check_collisions()
        
        # Check if food has been eaten
        self.check_food()

    def check_collisions(self):
        """
        Checks if the snake has collided with the game boundaries (walls)
        or its own body (self-collision).
        """
        head = self.snake.head
        
        # 1. Wall Collision Check
        if head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT:
            self.game_over = True
            self.save_high_score()
            return

        # 2. Self Collision Check
        if self.snake.check_collision_with_self():
            self.game_over = True
            self.save_high_score()

    def check_food(self):
        """
        Checks if the snake's head matches the food's coordinates.
        If yes, triggers growth, updates score, checks for level up, and spawns new food.
        """
        head = self.snake.head
        if head.x == self.food[0] and head.y == self.food[1]:
            # Trigger growth for the next move
            self.snake.grow()
            
            # Increase score
            self.score += SCORE_PER_FOOD
            
            # Check if level needs to be increased
            self.check_level_up()
            
            # Spawn new food
            self.spawn_food()
            
            # Update High Score if current score exceeds it
            if self.score > self.high_score:
                self.high_score = self.score

    def check_level_up(self):
        """
        Increases game difficulty (speed) based on the score.
        """
        # Calculate expected level: 1 + (Score / Threshold)
        new_level = 1 + (self.score // LEVEL_THRESHOLD)
        
        if new_level > self.level:
            self.level = new_level
            # Increase game speed (Frame Rate)
            self.speed = INITIAL_SPEED + (self.level - 1) * SPEED_INCREMENT

    def load_high_score(self):
        """
        Loads the high score from a local JSON file.
        Returns 0 if file doesn't exist or is corrupt.
        """
        if os.path.exists("high_score.json"):
            try:
                with open("high_score.json", "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
            except:
                return 0
        return 0

    def save_high_score(self):
        """
        Saves the current high score to a local JSON file.
        """
        with open("high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def draw(self, screen, font):
        """
        Renders all game elements to the screen.
        """
        # 1. Draw Background (Checkered Pattern)
        screen.fill(COLOR_BG)
        for row in range(GRID_HEIGHT):
            if row % 2 == 0:
                for col in range(0, GRID_WIDTH, 2):
                    pygame.draw.rect(screen, COLOR_BG_EVEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            else:
                for col in range(1, GRID_WIDTH, 2):
                    pygame.draw.rect(screen, COLOR_BG_EVEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # 2. Draw Snake
        coords = self.snake.get_coordinates()
        for i, (x, y) in enumerate(coords):
            # Head is a different color than the body
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            # Draw snake segment with slight border radius for rounded look
            pygame.draw.rect(screen, color, rect, border_radius=5)
            
            # Draw Eyes (Only for the head)
            if i == 0:
                eye_radius = 4
                # Simple eye placement relative to the head block
                pygame.draw.circle(screen, (255, 255, 255), (x * GRID_SIZE + 10, y * GRID_SIZE + 10), eye_radius)
                pygame.draw.circle(screen, (255, 255, 255), (x * GRID_SIZE + 30, y * GRID_SIZE + 10), eye_radius)

        # 3. Draw Food
        # Draw food as a rounded rectangle (almost circle)
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, COLOR_FOOD, food_rect, border_radius=10) 

        # 4. Draw UI Elements (Score, Level, High Score)
        score_text = font.render(f"Score: {self.score}", True, COLOR_TEXT)
        level_text = font.render(f"Level: {self.level}", True, COLOR_TEXT)
        high_score_text = font.render(f"High Score: {self.high_score}", True, COLOR_TEXT)

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))

        # 5. Draw Game Over Overlay
        if self.game_over:
            # Create a semi-transparent black overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            # Draw Game Over Text
            game_over_text = font.render("GAME OVER", True, (255, 255, 255))
            restart_text = font.render("Press R to Restart", True, (255, 255, 255))
            
            # Center the text on screen
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 10))
