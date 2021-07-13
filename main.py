"""
A* Pathfinding Visualizer
---------
@author: "Arnav Jain"
@createdOn: 12/07/2021
---------
"""

# Code Start Here 👇

import pygame
import math
from queue import PriorityQueue
from Node import Node

print("initialized")

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Visualizer")

colors = {
    "red": (205, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (85, 85, 85),
    "purple": (128, 0, 128),
    "orange": (255, 165, 0),
    "grey": (128, 128, 128),
    "turquoise": (64, 224, 208),
    "hyper": (34, 34, 34)
}

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def makeGrid(rows, width):
    grid = []
    gap = width // rows

    for x in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(x, j, gap, rows)
            grid[x].append(node)

    return grid


def drawGrid(win, rows, width):
    gap = width // rows

    for x in range(rows):
        pygame.draw.line(win, colors["grey"], (0, x * gap), (width, x * gap))
        
        for x in range(rows):
            pygame.draw.line(win, colors["grey"], (x * gap, 0), (x * gap, width))


def draw(win, grid, rows, width):
    win.fill(colors["hyper"])

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()


def getClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = makeGrid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)

                node = grid[row][col]

                if not start:
                    start = node
                    start.setToStart()

                elif not end:
                    end = node
                    end.setToEnd()

                elif node != start and node != end:
                    node.setToBarrier()

            if pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()


main(WIN, WIDTH)