import pygame

RED = (236, 73, 73)
GREEN = (73, 236, 121)
BLUE = (240, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (73, 97, 236)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
	def __init__(self, row, col, width, totalRows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.totalRows = totalRows

	def getPos(self):
		return self.row, self.col

	def isClosed(self):
		return self.color == RED

	def isOpen(self):
		return self.color == GREEN

	def isBarrier(self):
		return self.color == BLACK

	def isStart(self):
		return self.color == BLUE

	def isEnd(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def close(self):
		self.color = RED

	def setOpen(self):
		self.color = GREEN

	def setToBarrier(self):
		self.color = BLACK

	def setToStart(self):
		self.color = BLUE

	def setToEnd(self):
		self.color = TURQUOISE

	def setToPath(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def updateNeighbors(self, grid):
		self.neighbors = []

		if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.row > 0 and not grid[self.row][self.col - 1].isBarrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False
