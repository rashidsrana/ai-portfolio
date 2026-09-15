"""
Task 1: Robot Fault Detection using Random Forest
A robotic arm in a manufacturing unit sometimes performs faulty movements due to sensor noise. The company has collected labeled data of “Normal” and “Faulty” operations based on joint angles, motor current, and temperature.
Use a given dataset to train a Random Forest Classifier to detect faulty movements.
Test the model with new inputs and report accuracy.
data = [[30, 2.1, 35], [90, 4.5, 60], [45, 2.3, 36], [85, 5.0, 62]]
labels = ['Normal', 'Faulty', 'Normal', 'Faulty']
Test on this Data – [40, 2.5, 37]
"""

from sklearn.ensemble import RandomForestClassifier

# ================================
# Task 1: Robot Fault Detection
# ================================

# Training Data
data = [
    [30, 2.1, 35],  # Normal
    [90, 4.5, 60],  # Faulty
    [45, 2.3, 36],  # Normal
    [85, 5.0, 62],  # Faulty
]

labels = ["Normal", "Faulty", "Normal", "Faulty"]

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(data, labels)

# Test Input
test_input = [[40, 2.5, 37]]

# Prediction
prediction = model.predict(test_input)
print("Prediction for test input:", prediction[0])

# Accuracy (on training data)
accuracy = model.score(data, labels)
print("Training Accuracy:", accuracy)
