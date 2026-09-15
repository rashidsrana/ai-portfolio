"""
Automatic Moving Robots
You are programming a robot to move in a grid environment. The grid has free spaces (0) and obstacles (1). Your task is to write a program that checks whether a given position in the grid is free or blocked by an obstacle. The robot needs to decide if it can move to that position or not.

The program should:

Accept coordinates (x, y).

Check if the position is inside the grid.

Tell if the position is free or an obstacle.

[0, 0, 0, 1, 0]
[0, 1, 0, 0, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 0]

"""

# ============================================
# Automatic Moving Robots – Grid Position Check
# ============================================

# Grid (0 = free, 1 = obstacle)
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

def check_position(x, y):
    rows = len(grid)
    cols = len(grid[0])

    # Step 1: Check if inside grid
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return "Position is outside the grid."

    # Step 2: Check if free or obstacle
    if grid[x][y] == 0:
        return "Position is free. Robot can move."
    else:
        return "Position is blocked by an obstacle."

# ============================
# Test the function
# ============================

print(check_position(0, 3))   # obstacle
print(check_position(1, 0))   # free
print(check_position(4, 4))   # free
print(check_position(10, 2))  # outside grid
