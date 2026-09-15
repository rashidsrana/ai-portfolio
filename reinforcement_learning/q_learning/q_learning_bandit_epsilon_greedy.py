"""
This code implements a simple Q-learning algorithm for a two-action bandit problem using an epsilon-greedy strategy. The agent learns to choose between two machines (A and B) based on the rewards received from each action.
"""

import random

Q = [0, 0]  # Q-values for actions A and B
alpha = 0.1  # Learning rate
epsilon = 0.1  # Exploration rate


def get_reward(action):
    if action == 0:
        return random.choice([0, 1])  # Machine A: random reward
    else:
        return 1  # Machine B: always reward 1


for episode in range(50):

    # Epsilon-greedy action selection
    if random.random() < epsilon:
        action = random.choice([0, 1])  # Explore
    else:
        action = Q.index(max(Q))  # Exploit

    reward = get_reward(action)

    # Q-learning update
    Q[action] = Q[action] + alpha * (reward - Q[action])

print("Final Q-values:", Q)

best = "A" if Q[0] > Q[1] else "B"
print("Best machine:", best)
