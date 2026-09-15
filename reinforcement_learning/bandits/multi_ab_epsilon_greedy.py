"""
✔ Multi‑Armed Bandit Problem
You have multiple choices (slot machines), each with unknown reward probabilities.
Your goal is to learn which machine gives the highest reward.

✔ Epsilon‑Greedy Algorithm
This algorithm balances:

Exploration (try random machines to gather information)

Exploitation (choose the machine with the highest average reward so far)

Your code does exactly this:

With probability epsilon = 0.2, it explores (chooses randomly)

With probability 0.8, it exploits (chooses the machine with the highest average reward)

This is one of the simplest and most widely used RL strategies.
"""

import random

# Probabilities of reward
machines = [0.1, 0.4, 0.9]

# Store rewards and counts
rewards = [0, 0, 0]
counts = [0, 0, 0]

epsilon = 0.2

for step in range(100):

    # Exploration
    if random.random() < epsilon:
        choice = random.randint(0, 2)

    # Exploitation
    else:
        averages = []
        for i in range(3):
            if counts[i] == 0:
                averages.append(0)
            else:
                averages.append(rewards[i] / counts[i])

        choice = averages.index(max(averages))

    # Simulate reward
    if random.random() < machines[choice]:
        reward = 1
    else:
        reward = 0

    rewards[choice] += reward
    counts[choice] += 1

    print("Step:", step, "Machine:", choice, "Reward:", reward)

print("\nAverage Rewards:")

for i in range(3):
    if counts[i] == 0:
        avg = 0
    else:
        avg = rewards[i] / counts[i]

    print("Machine", i, "=", avg)
