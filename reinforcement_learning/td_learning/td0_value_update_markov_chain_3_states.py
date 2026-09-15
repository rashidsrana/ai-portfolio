"""
TD(0) Value Update in a Markov Chain with 3 States
"""

alpha = 2
gamma = 1
episodes = 10

# Initialize value function
V = {"H": 0, "W": 0, "F": 0}

for _ in range(episodes):

    # Transition H → W with reward 0
    V["H"] = V["H"] + alpha * (0 + gamma * V["W"] - V["H"])

    # Transition W → F with reward -10
    V["W"] = V["W"] + alpha * (-10 + gamma * V["F"] - V["W"])

print("Final Values:")
print(V)
