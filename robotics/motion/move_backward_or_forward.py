"""
Task 2: Move Backward or Forward
Objective: Update the robot's position based on user input.

Instructions:

Start the robot at position 0.

Ask the user to enter a number of steps.

Ask the user to enter a direction:

"F" for Forward

"B" for Backward

If the direction is "F", increase the position by the entered steps.

If the direction is "B", decrease the position by the entered steps.


================================
"""

# Task 2: Move Backward or Forward

# 1. Start at position 0
position = 0

# 2. Ask user for number of steps
steps = int(input("Enter number of steps: "))

# 3. Ask user for direction
direction = input("Enter direction (F for Forward, B for Backward): ").upper()

# 4–5. Update position based on direction
if direction == "F":
    position += steps
elif direction == "B":
    position -= steps
else:
    print("Invalid direction entered.")

# 6. Print final position
print("Final Position:", position)
