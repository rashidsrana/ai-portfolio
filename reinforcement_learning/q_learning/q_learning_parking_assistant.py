import random
import numpy as np

# -----------------------------------------
# Smart Parking Assistant — Approximate Q-Learning
# -----------------------------------------

# States
FAR = 0
NEAR = 1
AVAILABLE = 2
PARKED = 3

# Actions
ACTIONS = ["forward", "backward", "park"]

# Rewards
REWARD_SUCCESS = 10
REWARD_FOUND = 5
REWARD_DRIVE = -1
REWARD_WRONG = -3


# Feature extractor
def extract_features(state, action):
    return np.array(
        [
            1.0,  # bias term
            state == FAR,  # far
            state == NEAR,  # near
            state == AVAILABLE,  # spot available
            action == "park",  # parking attempt
        ],
        dtype=float,
    )


# Initialize weights
weights = np.zeros(5)


# Q-value approximation
def Q_value(state, action):
    features = extract_features(state, action)
    return np.dot(weights, features)


# Choose best action
def best_action(state):
    q_vals = {a: Q_value(state, a) for a in ACTIONS}
    return max(q_vals, key=q_vals.get)


# Transition model
def transition(state, action):
    if state == PARKED:
        return PARKED, 0

    if action == "park":
        if state == AVAILABLE:
            return PARKED, REWARD_SUCCESS
        else:
            return state, REWARD_WRONG

    if action == "forward":
        if state == FAR:
            return NEAR, REWARD_DRIVE
        elif state == NEAR:
            return AVAILABLE, REWARD_FOUND
        else:
            return AVAILABLE, REWARD_DRIVE

    if action == "backward":
        return FAR, REWARD_DRIVE

    return state, 0


# Training parameters
alpha = 0.1
gamma = 0.9
episodes = 50

# Training loop
for ep in range(episodes):
    state = FAR

    while state != PARKED:
        action = best_action(state)
        next_state, reward = transition(state, action)

        # TD target
        target = reward + gamma * max(Q_value(next_state, a) for a in ACTIONS)

        # TD error
        prediction = Q_value(state, action)
        error = target - prediction

        # Update weights
        weights += alpha * error * extract_features(state, action)

        state = next_state

print("\nLearned Weights:", weights)

# Test policy
print("\nLearned Policy:")
for s in [FAR, NEAR, AVAILABLE]:
    print(f"State {s} → Action: {best_action(s)}")
