"""
1. Set Robot Position
Create three variables: x, y, and z.

Assign the values:
• x = 150
• y = 80
• z = 250

Print the robot’s position.

2. Update Position
Set the robot’s initial position to:
• x = 300
• y = 100
• z = 50

Increase the X position by 75.

Print the updated position.

3. Move Along X-Axis
Start at x = 20.

Increase X by 40 five times using a loop.

Print the position after each move.
"""

# Task 1: Set Robot Position

x = 150
y = 80
z = 250

print("Robot Position:", x, y, z)

# Task 2: Update Position

x = 300
y = 100
z = 50

# Increase X by 75
x += 75

print("Updated Position:", x, y, z)

# Task 3: Move Along X-Axis

x = 20  # Start at 20

for i in range(5):
    x += 40
    print("Position after move", i + 1, ":", x)
