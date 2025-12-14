# Python Snake Game with Linked List - Project Documentation

This project is a classic Snake game developed using the Python programming language and the Pygame library. The main objective of the project is to demonstrate how the **Linked List** data structure is used in a real-world application.

## Installation and Execution

1. Ensure Python is installed.
2. Install the required library:
   ```bash
   pip install pygame
   ```
3. Start the game:
   ```bash
   python main.py
   ```

## Project Structure

### 1. `snake_ll.py` (Linked List Implementation)
The snake's body is represented by a dynamic data structure, the **Singly Linked List**.
- **Node Class:** Holds each snake segment (coordinates) and a reference to the next segment (`next`).
- **SnakeLinkedList Class:**
    - `head`: The head of the snake (where new nodes are added based on movement direction).
    - `tail`: The tail of the snake (removed at each step).
    - `move()`: Adds a new node to the head (Head Insertion) and, if no food was eaten, removes the tail (Tail Deletion). This attempts to be done in **O(1)** complexity (for insertion).
    - `grow()`: Allows the snake to grow (skips the tail deletion step for one move).

### 2. `game_logic.py` (Game Logic)
The game rules are processed here.
- **Game Class:**
    - `spawn_food()`: Generates random food ensuring it doesn't appear on the snake's body.
    - `check_collisions()`: Checks for collisions with walls or the snake itself.
    - `update()`: The logical update step of the game loop.
    - **Level System:** Level increases every 50 points, increasing the game speed (`FPS`).
    - **High Score:** The highest score is stored in the `high_score.json` file.

### 3. `utils.py` (Constants)
Constant values such as game colors, screen dimensions, and direction vectors are kept here. This allows design changes to be managed from a single file.

## Algorithm Details

### Why Linked List?
The Snake game is an excellent example to demonstrate **Queue** or **Linked List** logic in data structures courses.
- When the snake moves, a new square is effectively added to the head, and a square is removed from the tail.
- If we used an Array (List), we might need to shift all elements at each step, which would cause performance loss.
- With a Linked List, adding and removing elements is done quickly via pointer changes.

### Animation and Visuals
A grid-based but visually appealing design was created using Pygame's drawing library.
- **Colors:** Soft and vibrant colors inspired by Google's Snake game were used.
- **Eyes:** Eyes were added to indicate the direction the snake is moving.

## Developer Notes
Since this is a student project, the code has been kept modular and readable. Each function has documentation strings (docstrings) explaining what it does.
