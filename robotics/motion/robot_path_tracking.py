"""
Python solution of it
Task 1: Robot Path Tracking  
Objective: Track the robot's position after a series of movements.

Instructions:

Start the robot at position 0.

Use the movement list:
moves = ["up", "up", "up", "down", "down"]

Increase the position by 1 for every "up" move.

Decrease the position by 1 for every "down" move.

Display the position after each move.

Display the final position at the end.
"""

# Task 1: Robot Path Tracking

# 1. Start the robot at position 0
position = 0

# 2. Movement list
moves = ["up", "up", "up", "down", "down"]

# 3–5. Process each move and display position after each step
for move in moves:
    if move == "up":
        position += 1
    elif move == "down":
        position -= 1
    
    print("Position after", move, ":", position)

# 6. Display final position
print("\nFinal Position:", position)
