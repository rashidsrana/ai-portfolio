"""
Task 1: Constant Acceleration Movement
A small delivery robot works inside a large warehouse. It starts from complete rest and gradually speeds up at a constant rate for five seconds without stopping. Its speed increases steadily every second.

Your task:  
Draw a graph showing how the robot’s speed increases over time.
"""

import matplotlib.pyplot as plt

# ============================================
# Task 1: Constant Acceleration Movement
# ============================================

# Robot starts from rest
initial_speed = 0          # m/s
acceleration = 2           # m/s^2 (constant)
time_seconds = [0, 1, 2, 3, 4, 5]

# Calculate speed at each second: v = u + at
speeds = [initial_speed + acceleration * t for t in time_seconds]

# Print values
print("Time (s):", time_seconds)
print("Speed (m/s):", speeds)

# Plot speed-time graph
plt.plot(time_seconds, speeds, marker='o', linestyle='-', color='blue')
plt.title("Robot Speed vs Time (Constant Acceleration)")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (m/s)")
plt.grid(True)
plt.show()


