# AStar-Visualizer

## Explanation 👇
- The A* algorithm is used to determine the best path to any node or location on a graph. It is one of the fastes algorithms out there.
- Unlike Dijkstra's Algorithm, A* doesn't map through every node but instead uses a heristic function to determine the direction of the goal.
- After that is done, it moves to the neighbor of the last node that was in check and checks for the direction of the goal again.
- The time complexity for A* depends on the heuristic function, in this case its `O(bd)`
- My application here uses pygame and OOP to visualize A*

## Modules Used 👇
- Pygame
- Queue
- Math

## Run the program for yourself 👇
- Clone the files onto your desktop
- Open your editor
- To run from the terminal type `python main.py` or simply run the program using the IDE. 