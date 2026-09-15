import random

# Q-table: 3 states, 2 actions (left=0, right=1)
Q = [[0, 0] for _ in range(3)]

alpha = 0.1
gamma = 0.9
epsilon = 0.2
goal = 2


def step(state, action):
    # Action 1 = move right, Action 0 = move left
    if action == 1:
        next_state = min(state + 1, 2)
    else:
        next_state = max(state - 1, 0)

    # Reward only when reaching the goal
    reward = 10 if next_state == goal else 0
    return next_state, reward


# Training loop
for episode in range(30):
    state = 0

    while state != goal:

        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = Q[state].index(max(Q[state]))

        # Environment step
        next_state, reward = step(state, action)

        # Q-learning update
        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max(Q[next_state]) - Q[state][action]
        )

        state = next_state

# Final Q-table
print("\nFinal Q-table:")
for i, q in enumerate(Q):
    print(f"State {i}: {q}")
