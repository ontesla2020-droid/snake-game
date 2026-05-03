import pygame
import random

# --- SETTINGS ---
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED   = (200, 0, 0)
GRAY  = (40, 40, 40)

FPS = 10

# --- PYGAME SETUP ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Om's Snake Game 🐍")
clock = pygame.time.Clock()

# --- SNAKE SETUP ---
snake = [
    [10, 10],
    [9, 10],
    [8, 10],
]
direction = [1, 0]

# --- FOOD SETUP ---
def spawn_food():
    cols = WINDOW_WIDTH // CELL_SIZE
    rows = WINDOW_HEIGHT // CELL_SIZE
    return [random.randint(0, cols - 1), random.randint(0, rows - 1)]

food = spawn_food()

# --- DRAW FUNCTIONS ---
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

def draw_snake(snake):
    for i, segment in enumerate(snake):
        x = segment[0] * CELL_SIZE
        y = segment[1] * CELL_SIZE
        color = (0, 255, 0) if i == 0 else (0, 180, 0)
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

def draw_food(food):
    x = food[0] * CELL_SIZE
    y = food[1] * CELL_SIZE
    pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def check_collision(snake):
    head = snake[0]
    cols = WINDOW_WIDTH // CELL_SIZE
    rows = WINDOW_HEIGHT // CELL_SIZE
    if head[0] < 0 or head[0] >= cols or head[1] < 0 or head[1] >= rows:
        return True
    if head in snake[1:]:
        return True
    return False

# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]

    # Move snake
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, new_head)

    # Check if food eaten
    if new_head == food:
        food = spawn_food()
    else:
        snake.pop()

    # Check collision
    if check_collision(snake):
        print(f"Game Over! Score: {len(snake) - 3}")
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    draw_snake(snake)
    draw_food(food)
    draw_score(len(snake) - 3)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
