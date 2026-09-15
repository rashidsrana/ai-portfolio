"""
Automatic Moving Robots
The function worked like this: Robo would take 5 equal steps to return to the starting point. With every step, Robo would reduce his position by 2, starting from 10. The engineer’s plan was clear and efficient, and Robo trusted the function to guide him safely.

Starting at position 10, Robo moved 2 units back, landing at position 8.

His second step took him to position 6.

The third step brought him to position 4.

Then, he stepped to position 2.

Finally, Robo took his last step and reached position 0, completing his journey.
"""

# Automatic Moving Robots

position = 10          # Starting position
steps = 5              # Total steps
step_size = 2          # Reduce by 2 each step

positions = []         # To store visited positions

for i in range(steps):
    position -= step_size
    positions.append(position)

print("Robo's movement:")
for p in positions:
    print(p)
