# Renkler (Google Snake benzeri canlı renkler)
COLOR_BG = (170, 215, 81)       # Açık yeşil (Zemin)
COLOR_BG_EVEN = (162, 209, 73)  # Koyu yeşil (Damalı zemin için)
COLOR_SNAKE = (78, 124, 246)    # Mavi (Yılan gövdesi)
COLOR_SNAKE_HEAD = (60, 90, 200) # Koyu Mavi (Yılan başı)
COLOR_FOOD = (231, 71, 29)      # Kırmızı (Elma)
COLOR_TEXT = (255, 255, 255)    # Beyaz

# Ekran Ayarları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 40  # Karenin boyutu (Yılanın kalınlığı)
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Yönler
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Oyun Ayarları
INITIAL_SPEED = 5
SPEED_INCREMENT = 1  # Her levelde artacak hız miktarı
SCORE_PER_FOOD = 10
LEVEL_THRESHOLD = 50 # Her 50 puanda bir level atlar
