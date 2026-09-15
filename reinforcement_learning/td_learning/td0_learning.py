# TD(0) Simple Example

import numpy as np

states = ["A", "B", "C"]

# Initialize value function
V = {"A": 0.0, "B": 0.0, "C": 0.0}

alpha = 0.5  # learning rate
gamma = 1.0  # discount factor
episodes = 5

for ep in range(episodes):
    print(f"\nEpisode {ep+1}")

    # Transition A -> B with reward 0
    reward = 0
    V["A"] = V["A"] + alpha * (reward + gamma * V["B"] - V["A"])

    # Transition B -> C with reward 10
    reward = 10
    V["B"] = V["B"] + alpha * (reward + gamma * V["C"] - V["B"])

    print(V)

print("\nFinal Values:", V)
