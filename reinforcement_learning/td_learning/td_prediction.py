# TD(0) for Traffic Light Congestion Learning

alpha = 0.5  # learning rate
gamma = 1.0  # discount factor
episodes = 10

# Initialize value estimates
V = {"G": 0.0, "Y": 0.0, "R": 0.0}

for ep in range(episodes):
    print(f"\nEpisode {ep+1}")

    # G → Y (reward = 0)
    reward = 0
    V["G"] = V["G"] + alpha * (reward + gamma * V["Y"] - V["G"])

    # Y → R (reward = -5)
    reward = -5
    V["Y"] = V["Y"] + alpha * (reward + gamma * V["R"] - V["Y"])

    # R → terminal (reward = 0)
    reward = 0
    V["R"] = V["R"] + alpha * (reward + gamma * 0 - V["R"])

    print(V)

print("\nFinal Learned Values:")
print(V)
