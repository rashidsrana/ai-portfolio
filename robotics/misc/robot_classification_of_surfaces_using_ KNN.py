"""
Task 2: 	Robot Classification of Surfaces using KNN
A mobile robot has a surface sensor to detect terrain types (e.g., wood, carpet, tile) for traction control. The sensor gives three readings: roughness, color intensity, and temperature.
Objective
Use K-Nearest Neighbors (KNN) to classify surface type from sensor readings.
Train with example data and predict class for new inputs.
python
CopyEdit
data = [[0.2, 150, 22], [0.8, 100, 25], [0.1, 170, 21], [0.85, 95, 26]]
labels = ['tile', 'carpet', 'wood', 'carpet']
Test on this Data – [0.15, 160, 22]

"""

from sklearn.neighbors import KNeighborsClassifier

# ============================================
# Robot Surface Classification using KNN
# ============================================

# Training Data: [roughness, color_intensity, temperature]
data = [
    [0.2, 150, 22],  # tile
    [0.8, 100, 25],  # carpet
    [0.1, 170, 21],  # wood
    [0.85, 95, 26],  # carpet
]

labels = ["tile", "carpet", "wood", "carpet"]

# Create and train the KNN model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(data, labels)

# Test Input
test_input = [[0.15, 160, 22]]

# Prediction
prediction = model.predict(test_input)
print("Prediction for test input:", prediction[0])

# Accuracy (on training data)
accuracy = model.score(data, labels)
print("Training Accuracy:", accuracy)
