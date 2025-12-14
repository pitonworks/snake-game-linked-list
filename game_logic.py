import random
import json
import os
import pygame
from snake_ll import SnakeLinkedList
from utils import *

class Game:
    def __init__(self):
        self.snake = SnakeLinkedList()
        self.food = None
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED
        self.game_over = False
        self.high_score = self.load_high_score()
        self.spawn_food()

    def spawn_food(self):
        """
        Yılanın üzerine gelmeyecek şekilde rastgele bir yerde yem oluşturur.
        """
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # Yılanın üstünde mi kontrol et
            on_snake = False
            current = self.snake.head
            while current is not None:
                if current.x == x and current.y == y:
                    on_snake = True
                    break
                current = current.next
            
            if not on_snake:
                self.food = (x, y)
                break

    def handle_input(self, event):
        """
        Klavye girişlerini işler.
        Zıt yönlere ani dönüşü engeller.
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
        Oyun durumunu günceller.
        """
        if self.game_over:
            return

        self.snake.move()
        self.check_collisions()
        self.check_food()

    def check_collisions(self):
        """
        Duvara veya kendine çarpma kontrolü.
        """
        head = self.snake.head
        
        # Duvar kontrolü
        if head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT:
            self.game_over = True
            self.save_high_score()
            return

        # Kendine çarpma kontrolü
        if self.snake.check_collision_with_self():
            self.game_over = True
            self.save_high_score()

    def check_food(self):
        """
        Yem yendi mi kontrolü.
        """
        head = self.snake.head
        if head.x == self.food[0] and head.y == self.food[1]:
            self.snake.grow()
            self.score += SCORE_PER_FOOD
            self.check_level_up()
            self.spawn_food()
            
            # High Score güncelle
            if self.score > self.high_score:
                self.high_score = self.score

    def check_level_up(self):
        """
        Skora göre seviye ve hız artırır.
        """
        new_level = 1 + (self.score // LEVEL_THRESHOLD)
        if new_level > self.level:
            self.level = new_level
            self.speed = INITIAL_SPEED + (self.level - 1) * SPEED_INCREMENT

    def load_high_score(self):
        if os.path.exists("high_score.json"):
            try:
                with open("high_score.json", "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
            except:
                return 0
        return 0

    def save_high_score(self):
        with open("high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def draw(self, screen, font):
        # Arka plan (Damalı desen)
        screen.fill(COLOR_BG)
        for row in range(GRID_HEIGHT):
            if row % 2 == 0:
                for col in range(0, GRID_WIDTH, 2):
                    pygame.draw.rect(screen, COLOR_BG_EVEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            else:
                for col in range(1, GRID_WIDTH, 2):
                    pygame.draw.rect(screen, COLOR_BG_EVEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Yılanı çiz
        coords = self.snake.get_coordinates()
        for i, (x, y) in enumerate(coords):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, color, rect, border_radius=5)
            
            # Gözler (Sadece kafa için)
            if i == 0:
                eye_radius = 4
                # Yöne göre göz pozisyonu ayarlanabilir ama şimdilik basit tutuyoruz
                pygame.draw.circle(screen, (255, 255, 255), (x * GRID_SIZE + 10, y * GRID_SIZE + 10), eye_radius)
                pygame.draw.circle(screen, (255, 255, 255), (x * GRID_SIZE + 30, y * GRID_SIZE + 10), eye_radius)

        # Yemi çiz
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, COLOR_FOOD, food_rect, border_radius=10) # Elma gibi yuvarlak

        # UI Çizimi
        score_text = font.render(f"Score: {self.score}", True, COLOR_TEXT)
        level_text = font.render(f"Level: {self.level}", True, COLOR_TEXT)
        high_score_text = font.render(f"High Score: {self.high_score}", True, COLOR_TEXT)

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))

        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(150)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            game_over_text = font.render("GAME OVER", True, (255, 255, 255))
            restart_text = font.render("Press R to Restart", True, (255, 255, 255))
            
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 10))
