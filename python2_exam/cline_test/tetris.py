import pygame
import random

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [(0, 255, 255), (0, 0, 255), (255, 127, 0),
          (255, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 255)]

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 0], [0, 1, 1]],  # S
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[0, 1, 0], [1, 1, 1]]   # T
]


def create_grid(width, height):
    grid = [[0] * width for _ in range(height)]
    return grid


def draw_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != 0:
                pygame.draw.rect(
                    screen, COLORS[cell - 1], (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, (j * BLOCK_SIZE,
                                 i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            else:
                pygame.draw.rect(screen, GRAY, (j * BLOCK_SIZE,
                                 i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def new_piece():
    shape = random.choice(SHAPES)
    color = random.randint(1, len(COLORS))
    x = GRID_WIDTH // 2 - len(shape[0]) // 2
    y = 0
    return shape, color, x, y


def rotate(shape):
    rotated_shape = list(zip(*shape[::-1]))
    return rotated_shape


def valid_move(grid, shape, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                try:
                    if grid[y + offset_y][x + offset_x] != 0:
                        return False
                except IndexError:
                    return False
    return True


def place_piece(grid, shape, color, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset_y][x + offset_x] = color


def clear_lines(grid):
    lines_cleared = 0
    full_rows = [i for i, row in enumerate(grid) if all(row)]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)
        lines_cleared += 1
    return lines_cleared


def game_over(grid):
    return any(grid[0])


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    grid = create_grid(GRID_WIDTH, GRID_HEIGHT)
    shape, color, x, y = new_piece()
    drop_time = 0
    drop_speed = 0.5
    score = 0

    running = True
    while running:
        screen.fill(BLACK)
        draw_grid(screen, grid)

        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen, COLORS[color - 1], ((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, WHITE, ((
                        x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_move(grid, shape, x - 1, y):
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if valid_move(grid, shape, x + 1, y):
                        x += 1
                if event.key == pygame.K_DOWN:
                    if valid_move(grid, shape, x, y + 1):
                        y += 1
                if event.key == pygame.K_UP:
                    rotated_shape = rotate(shape)
                    if valid_move(grid, rotated_shape, x, y):
                        shape = rotated_shape

        drop_time += clock.get_rawtime()
        clock.tick()

        if drop_time / 1000 > drop_speed:
            drop_time = 0
            if valid_move(grid, shape, x, y + 1):
                y += 1
            else:
                place_piece(grid, shape, color, x, y)
                lines_cleared = clear_lines(grid)
                score += lines_cleared * 100
                shape, color, x, y = new_piece()
                if game_over(grid):
                    print("Game Over! Score:", score)
                    running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
