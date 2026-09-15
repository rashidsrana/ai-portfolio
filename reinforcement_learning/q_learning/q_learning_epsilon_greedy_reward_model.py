import random

Q = [0, 0]  # Q-values for actions A and B
alpha = 0.1  # Learning rate
epsilon = 0.2  # Exploration rate

for episode in range(20):

    # Epsilon-greedy action selection
    if random.random() < epsilon:
        action = random.randint(0, 1)  # Explore
    else:
        action = Q.index(max(Q))  # Exploit

    # Reward model
    if action == 0:
        reward = 1  # A is good
    else:
        reward = 0  # B is bad

    # Q-learning update
    Q[action] = Q[action] + alpha * (reward - Q[action])

    print(f"Episode {episode+1}: Action={action}, Q={Q}")

print("\nFinal Q-values:", Q)
print("Best action:", "A" if Q[0] > Q[1] else "B")
