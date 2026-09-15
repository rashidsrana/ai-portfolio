import random
import numpy as np

# -----------------------------------------
# Drone Package Delivery — FINAL STABLE VERSION
# -----------------------------------------

# States
WAREHOUSE = 0
EN_ROUTE = 1
NEAR_DEST = 2
DELIVERED = 3

# Actions
ACTIONS = ["forward", "return", "deliver"]

# Rewards
REWARD_SUCCESS = 10
REWARD_REACH = 5
REWARD_FLY = -1
REWARD_WRONG = -4


# Normalized feature extractor
def extract_features(state, battery):
    distance_map = {WAREHOUSE: 1.0, EN_ROUTE: 0.5, NEAR_DEST: 0.1, DELIVERED: 0.0}
    return np.array([distance_map[state], battery], dtype=float)


# Initialize weights small
weights = np.array([0.001, 0.001])


# Q-value approximation
def Q_value(state, action, battery):
    return np.dot(weights, extract_features(state, battery))


# Epsilon-greedy action selection
def choose_action(state, battery, epsilon=0.1):
    if random.random() < epsilon:
        return random.choice(ACTIONS)
    return max(ACTIONS, key=lambda a: Q_value(state, a, battery))


# Transition model
def transition(state, action, battery):
    if state == DELIVERED:
        return DELIVERED, 0, battery

    if action == "deliver":
        if state == NEAR_DEST:
            return DELIVERED, REWARD_SUCCESS, battery
        else:
            return state, REWARD_WRONG, battery

    if action == "forward":
        if state == WAREHOUSE:
            return EN_ROUTE, REWARD_FLY, battery - 0.02
        elif state == EN_ROUTE:
            return NEAR_DEST, REWARD_REACH, battery - 0.02
        elif state == NEAR_DEST:
            return NEAR_DEST, REWARD_FLY, battery - 0.02

    if action == "return":
        return WAREHOUSE, REWARD_FLY, battery - 0.02

    return state, 0, battery


# Training parameters
alpha = 0.005  # VERY small learning rate
gamma = 0.9
episodes = 200

# Training loop
for ep in range(episodes):
    state = WAREHOUSE
    battery = 1.0

    steps = 0
    while state != DELIVERED and steps < 50:  # prevent infinite loops
        action = choose_action(state, battery)
        next_state, reward, next_battery = transition(state, action, battery)

        # TD target
        target = reward + gamma * max(
            Q_value(next_state, a, next_battery) for a in ACTIONS
        )

        # TD error
        prediction = Q_value(state, action, battery)
        error = target - prediction

        # Update weights
        weights += alpha * error * extract_features(state, battery)

        # Weight decay (prevents explosion)
        weights *= 0.99

        # Hard clipping
        weights = np.clip(weights, -5, 5)

        state = next_state
        battery = max(0.0, next_battery)
        steps += 1

print("\nLearned Weights:", weights)

# Test policy
print("\nLearned Policy:")
for s in [WAREHOUSE, EN_ROUTE, NEAR_DEST]:
    print(f"State {s} → Action: {choose_action(s, 1.0, epsilon=0.0)}")
