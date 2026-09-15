"""
Task 2: Reach the Target
The robot starts at position (0, 0).
It must reach the target at position (3, 3).

The robot can move up, down, left, or right, but:

It cannot move into obstacles (represented by 1)

It cannot move outside the grid

Your task is to find a valid path from the start to the target and print the sequence of positions the robot visits.
"""

# Task 2: Reach the Target

from collections import deque

# Example grid (0 = empty, 1 = obstacle)
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
target = (3, 3)

rows = len(grid)
cols = len(grid[0])

# Directions: up, down, left, right
directions = [(0,1), (0,-1), (1,0), (-1,0)]

# BFS queue
queue = deque([(start, [start])])
visited = set([start])

found_path = None

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == target:
        found_path = path
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Check boundaries and obstacles
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

# Print result
if found_path:
    print("Path to target:")
    for pos in found_path:
        print(pos)
else:
    print("No valid path found.")
