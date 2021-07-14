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

RED = (236, 73, 73)
GREEN = (73, 236, 121)
BLUE = (73, 151, 236)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def constructPath(cameFrom, current, draw, start):
    while current in cameFrom and current != start:
        current = cameFrom[current]
        current.setToPath()
        draw()


def algorithm(draw, grid, start, end):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))

    cameFrom = {}

    gScore = { node: float("inf") for row in grid for node in row }
    gScore[start] = 0

    fScore = { node: float("inf") for row in grid for node in row }
    fScore[start] = h(start.getPos(), end.getPos())

    openSetHash = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)

        if current == end:
            constructPath(cameFrom, end, draw, start)
            end.setToEnd()
            return True

        for neighbor in current.neighbors:
            temporaryGScore = gScore[current] + 1

            if temporaryGScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = temporaryGScore
                fScore[neighbor] = temporaryGScore + h(neighbor.getPos(), end.getPos())

                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    neighbor.setOpen()

        draw()

        if current != start:
            current.close()

    return False


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
        pygame.draw.line(win, GREY, (0, x * gap), (width, x * gap))
        
        for x in range(rows):
            pygame.draw.line(win, GREY, (x * gap, 0), (x * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

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

                if not start and node != end:
                    start = node
                    start.setToStart()

                elif not end and node != start:
                    end = node
                    end.setToEnd()

                elif node != start and node != end:
                    node.setToBarrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)

                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = makeGrid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)