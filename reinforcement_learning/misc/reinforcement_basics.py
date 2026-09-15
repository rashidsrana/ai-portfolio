import random

rewards = [0, 0, 0]
counts = [0, 0, 0]

for i in range(100):

    action = random.randint(0, 2)

    if action == 2:
        reward = 1
    else:
        reward = 0

    counts[action] += 1
    rewards[action] += reward

for i in range(3):
    print(f"Action {i}: Avg Reward = {rewards[i]/counts[i]:.2f}")
