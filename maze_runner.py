import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Maze layout (1 = wall, 0 = path)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Player settings
player_pos = [1, 1]  # Starting position
goal_pos = [7, 18]  # Goal position


def draw_maze():
    """Draw the maze layout on the screen."""
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if MAZE[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_player():
    """Draw the player on the screen."""
    pygame.draw.rect(
        screen, BLUE, (player_pos[1] * GRID_SIZE + 5, player_pos[0] * GRID_SIZE + 5, GRID_SIZE - 10, GRID_SIZE - 10)
    )


def draw_goal():
    """Draw the goal on the screen."""
    pygame.draw.rect(
        screen, GREEN, (goal_pos[1] * GRID_SIZE + 5, goal_pos[0] * GRID_SIZE + 5, GRID_SIZE - 10, GRID_SIZE - 10)
    )


# Game loop
running = True
while running:
    screen.fill(BLACK)
    draw_maze()
    draw_player()
    draw_goal()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        new_pos = [player_pos[0] - 1, player_pos[1]]
        if MAZE[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = [player_pos[0] + 1, player_pos[1]]
        if MAZE[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_LEFT]:
        new_pos = [player_pos[0], player_pos[1] - 1]
        if MAZE[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos
    if keys[pygame.K_RIGHT]:
        new_pos = [player_pos[0], player_pos[1] + 1]
        if MAZE[new_pos[0]][new_pos[1]] == 0:
            player_pos = new_pos

    # Check if the player reaches the goal
    if player_pos == goal_pos:
        print("You Win!")
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
