"""
Task 1: Stop When Position Reaches 15

Objective: Track the robot's position and stop when it reaches or exceeds 15.

Instructions:

Start the robot at position 0.

Use the list:

Code
steps = [2, 4, 3, 5, 1, 6]
Add each step to the position.

Print the position after each move.

If the position becomes 15 or more, print "Target Reached" and stop the loop using break.

Print the final position.
==================================
"""

# Task 1: Stop When Position Reaches 15

# 1. Start at position 0
position = 0

# 2. Step list
steps = [2, 4, 3, 5, 1, 6]

# 3–5. Add each step and stop when position >= 15
for step in steps:
    position += step
    print("Position after step:", position)

    if position >= 15:
        print("Target Reached")
        break

# 6. Final position
print("\nFinal Position:", position)
