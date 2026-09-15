"""
Task 2: Count Up and Down Movements
Objective: Count how many times the robot moves up and down.

Instructions:

Use the movement list:
moves = ["up", "down", "up", "up", "down", "up"]

Create variables to count:

Number of "up" moves.

Number of "down" moves.

Loop through the list and update the counters.

Print:

Total up moves.

Total down moves.

Final robot position (starting from 0).
"""

# Task 2: Count Up and Down Movements

# Movement list
moves = ["up", "down", "up", "up", "down", "up"]

# Counters
up_count = 0
down_count = 0

# Starting position
position = 0

# Loop through moves
for move in moves:
    if move == "up":
        up_count += 1
        position += 1
    elif move == "down":
        down_count += 1
        position -= 1

# Display results
print("Total up moves:", up_count)
print("Total down moves:", down_count)
print("Final robot position:", position)
