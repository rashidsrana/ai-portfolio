"""
Task 2: Robot Direction and Position Control
Objective: Update the robot's position based on movement commands.

Instructions:

Start with the robot at position 0.

Use the command list:

Code
commands = [
    ("forward", 4),
    ("forward", 3),
    ("backward", 2),
    ("forward", 5),
    ("backward", 1),
    ("forward", 6)
]
For each command:

If the command is "forward", increase the position by the given value.

If the command is "backward", decrease the position by the given value.

Print the command and the new position.

If the position becomes 10 or greater, print:

Code
Target reached!
and stop the robot.

If all commands are completed without reaching the target, print:

Code
Target not reached.
Finally, print the robot's final position.
"""

# Task 2: Robot Direction and Position Control

# 1. Start at position 0
position = 0

# 2. Command list
commands = [
    ("forward", 4),
    ("forward", 3),
    ("backward", 2),
    ("forward", 5),
    ("backward", 1),
    ("forward", 6)
]

# 3–4. Process each command
for direction, value in commands:
    if direction == "forward":
        position += value
    elif direction == "backward":
        position -= value

    print(f"Command: {direction}, New Position: {position}")

    if position >= 10:
        print("Target reached!")
        break

# 5. If loop completes without reaching target
else:
    print("Target not reached.")

# 6. Final position
print("Final Position:", position)
