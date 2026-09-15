# TD(0) — Coffee Machine Failure Learning

alpha = 0.5  # learning rate
gamma = 1.0  # discount factor
episodes = 10

# Initial value estimates
V = {"N": 0.0, "W": 0.0, "F": 0.0}

for ep in range(episodes):
    print(f"\nEpisode {ep+1}")

    # N → W (reward = 0)
    reward = 0
    V["N"] = V["N"] + alpha * (reward + gamma * V["W"] - V["N"])

    # W → F (reward = -10)
    reward = -10
    V["W"] = V["W"] + alpha * (reward + gamma * V["F"] - V["W"])

    # F → terminal (reward = 0)
    reward = 0
    V["F"] = V["F"] + alpha * (reward + gamma * 0 - V["F"])

    print(V)

print("\nFinal Learned Values:")
print(V)
