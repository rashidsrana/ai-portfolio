"""
Task
In the distant future, your robot Robo is exploring a maze to find hidden energy crystals.
The maze has obstacles in front and obstacles on the right. Robo must choose one of three actions:

Move Forward

Turn Right

Stop

But there’s a twist — Robo doesn’t know how to make decisions.

Your job is to train a Random Forest model so Robo can make smart choices based on its sensor data.
"""

from sklearn.ensemble import RandomForestClassifier

# ============================================================
# Random Forest Model for Robo's Maze Decisions
# ============================================================

# Training data (sensor inputs)
# front_clear, right_clear
# 1 = clear, 0 = obstacle

data = [
    [1, 1],   # Move Forward
    [1, 0],   # Move Forward
    [0, 1],   # Turn Right
    [0, 0],   # Stop
    [1, 1],   # Move Forward
    [0, 1],   # Turn Right
]

# Labels:
# 0 = Move Forward
# 1 = Turn Right
# 2 = Stop
labels = [0, 0, 1, 2, 0, 1]

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(data, labels)

# ============================================================
# Predict Robo's action for a new sensor reading
# ============================================================

# Example: front blocked, right clear
new_sensor = [[0, 1]]

prediction = model.predict(new_sensor)[0]

actions = {
    0: "Move Forward",
    1: "Turn Right",
    2: "Stop"
}

print("Sensor Input:", new_sensor[0])
print("Robo's Decision:", actions[prediction])

# Training accuracy
accuracy = model.score(data, labels)
print("Training Accuracy:", accuracy)
