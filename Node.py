import pygame

colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (73, 236, 156),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (85, 85, 85),
    "purple": (128, 0, 128),
    "orange": (255, 165, 0),
    "grey": (128, 128, 128),
    "turquoise": (73, 183, 236), 
    "hyper": (34, 34, 34)
}


class Node:
	def __init__(self, row, col, width, totalRows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = colors["white"]
		self.neighbors = []
		self.width = width
		self.totalRows = totalRows

	def getPos(self):
		return self.row, self.col

	def isClosed(self):
		return self.color == colors["red"]

	def isOpen(self):
		return self.color == colors["green"]

	def isBarrier(self):
		return self.color == colors["black"]

	def isStart(self):
		return self.color == colors["orange"]

	def isEnd(self):
		return self.color == colors["turquoise"]

	def reset(self):
		self.color = colors["white"]

	def close(self):
		self.color = colors["red"]

	def open(self):
		self.color = colors["green"]

	def setToBarrier(self):
		self.color = colors["green"]

	def setToStart(self):
		self.color = colors["orange"]

	def setToEnd(self):
		self.color = colors["turquoise"]

	def setToPath(self):
		self.color = colors["purple"]

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def updateNeighbors(self, grid):
		pass

	def __lt__(self, other):
		return False
