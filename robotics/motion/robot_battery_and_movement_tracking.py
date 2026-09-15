"""
Task 1: Robot Battery and Movement Tracking
Objective: Track the robot's position and battery level while moving.

Instructions:

Start the robot at position 0.

The robot has 100% battery.

Use the movement list:

Code
moves = [5, 3, 7, 2, 6]
For each movement:

Add the movement value to the robot's position.

Reduce the battery by 4%.

Print the current position and battery level.

If the battery becomes 20% or less, print:

Code
Low Battery! Robot must stop.
and stop processing any remaining movements.

Finally, print the total distance traveled.
"""

# Task 1: Robot Battery and Movement Tracking

# 1. Start robot at position 0
position = 0

# 2. Robot battery starts at 100%
battery = 100

# 3. Movement list
moves = [5, 3, 7, 2, 6]

# Track total distance
total_distance = 0

# 4–5. Process each movement
for move in moves:
    position += move
    battery -= 4
    total_distance += move

    print(f"Position: {position}, Battery: {battery}%")

    if battery <= 20:
        print("Low Battery! Robot must stop.")
        break

# 6. Final output
print("\nTotal Distance Traveled:", total_distance)
print("Final Position:", position)
