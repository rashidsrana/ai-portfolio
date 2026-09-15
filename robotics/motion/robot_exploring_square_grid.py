"""
Task
A small robot is exploring a square grid where some areas are free, and others have obstacles. The robot has collected data from several points and knows whether they are free or blocked. Now, the robot wants to predict whether a new location is safe to move to.

Your task is to help the robot by writing a Python program using the K-Nearest Neighbors (KNN) algorithm.
The program should:

Train a KNN model with sample data points (coordinates and labels: free or obstacle).

Take a new point as input.

Predict whether that new point is a free space or an obstacle using the model.

Print the result.

"""

from sklearn.neighbors import KNeighborsClassifier

# ============================================================
# KNN Model for Predicting Free vs Obstacle in a Grid
# ============================================================

# Sample training data (x, y coordinates + label)
# Label: 0 = free, 1 = obstacle
training_points = [
    [0, 0],   # free
    [1, 0],   # obstacle
    [2, 2],   # free
    [3, 1],   # obstacle
    [4, 4],   # free
    [1, 3],   # obstacle
]

labels = [0, 1, 0, 1, 0, 1]

# Create and train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(training_points, labels)

# ============================================================
# New point to predict
# ============================================================

new_point = [[2, 1]]   # Change this to test other coordinates

prediction = knn.predict(new_point)[0]

# Convert numeric label to text
result = "Free Space" if prediction == 0 else "Obstacle"

print("New Point:", new_point[0])
print("Prediction:", result)
