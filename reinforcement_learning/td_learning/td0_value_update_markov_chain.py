"""
TD(0) Value Update in a Markov Chain
"""

import numpy as np

# Initialize value function
V = {"R1": 0.0, "R2": 0.0, "R3": 0.0}

alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
episodes = 10

for ep in range(episodes):
    print(f"\nEpisode {ep+1}")

    # Transition R1 -> R2 with reward 0
    reward = 0
    V["R1"] = V["R1"] + alpha * (reward + gamma * V["R2"] - V["R1"])

    # Transition R2 -> R3 with reward 5
    reward = 5
    V["R2"] = V["R2"] + alpha * (reward + gamma * V["R3"] - V["R2"])

print(V)
print("\nFinal Values:", V)
