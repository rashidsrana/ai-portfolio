"""
Task 1: Move Right Until an Obstacle
The robot starts at position (1, 0).
It can only move right on the grid.

The robot keeps moving right until:

It reaches the edge of the grid, or

It encounters an obstacle (represented by the value 1).
"""

# Task 1: Move Right Until an Obstacle

# Example grid row (0 = empty, 1 = obstacle)
grid = [0, 0, 0, 0, 1, 0, 0]

# Robot starts at (1, 0)
x = 1
y = 0

visited_positions = []

# Move right until obstacle or edge
while x < len(grid) and grid[x] != 1:
    visited_positions.append((x, y))
    x += 1

# If robot stops because of obstacle, do not include obstacle position
print("Visited positions:")
for pos in visited_positions:
    print(pos)