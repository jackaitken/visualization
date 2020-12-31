import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("A* Search Visualization")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Square:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y  = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color == RED

    def make_open(self):
        self.color == GREEN

    def make_barrier(self):
        self.color == BLACK

    def make_start(self):
        self.color == ORANGE

    def make_end(self):
        self.color == TURQUOISE

    def make_path(self):
        self.color == PURPLE

    def draw(self, win):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

def heuristic(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            square = Square(i, j, gap, rows)
            grid[i].append(square)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(WIN, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(WIN, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    WIN.fill(WHITE)

    for row in grid:
        for square in row:
            square.draw(WIN)

    draw_grid(WIN, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None
    
    run = True
    started = False

    while run:
        draw(WIN, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            # check for left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                square = grid[row][col]
                if not start:
                    start = square
                    start.make_start()

                elif not end:
                    end = square
                    end.make_end()

                elif square != end and square != start:
                    square.make_barrier()

            # check for left right click
            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()

main(WIN, WIDTH)
