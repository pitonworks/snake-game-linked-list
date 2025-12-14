# Colors (Vibrant Google Snake-style palette)
COLOR_BG = (170, 215, 81)       # Light Green (Background)
COLOR_BG_EVEN = (162, 209, 73)  # Darker Green (For checkered pattern)
COLOR_SNAKE = (78, 124, 246)    # Blue (Snake Body)
COLOR_SNAKE_HEAD = (60, 90, 200) # Dark Blue (Snake Head)
COLOR_FOOD = (231, 71, 29)      # Red (Apple/Food)
COLOR_TEXT = (255, 255, 255)    # White (UI Text)

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 40  # Size of each grid square in pixels (Logic block size)

# Calculate grid dimensions based on screen size
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Direction Constants (x, y) changes
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game Configuration
INITIAL_SPEED = 5        # Initial frames per second (snake movement speed)
SPEED_INCREMENT = 1      # Amount to increase speed per level
SCORE_PER_FOOD = 10      # Points awarded for eating food
LEVEL_THRESHOLD = 50     # Score points needed to advance to the next level
