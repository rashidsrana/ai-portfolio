"""
1. Set Robot Position
Create three variables: x, y, and z.

Assign values and print the robot’s position.

2. Update Position
Set the robot’s initial position.

Increase the X position by 100 and print the updated position.

3. Move Along X-Axis
Start at x = 0.

Increase X by 50 five times using a loop.


"""

# Task 1: Set Robot Position

# Create variables
x = 10
y = 20
z = 30

# Print robot position
print("Robot Position:", x, y, z)

# Task 2: Update Position

# Initial position
x = 50
y = 20
z = 10

# Increase X by 100
x += 100

# Print updated position
print("Updated Position:", x, y, z)

# Task 3: Move Along X-Axis

x = 0  # Start at 0

# Increase X by 50 five times
for i in range(5):
    x += 50
    print("Position after move", i + 1, ":", x)
