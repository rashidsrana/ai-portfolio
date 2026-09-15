"""
Task: Object Recognition for Gripping (Numerical Data)
Data for Training the Random Forest Model:

Inputs (sensor data):

Weight: The weight of the object (in kilograms).

Height: The height of the object (in centimeters).

Width: The width of the object (in centimeters).

Density: The density of the object, calculated from weight and volume (in kg/m³).

Shape Factor: A numeric score representing the object's shape (e.g., spherical, cylindrical, rectangular) based on its dimensions.

Output (target label):

0: Object is a screwdriver.

1: Object is a ball.

2: Object is a box.
"""

from sklearn.ensemble import RandomForestClassifier

# ============================================================
# Object Recognition for Gripping using Random Forest
# ============================================================

# Training Data (example numerical values)
# Format: [weight, height, width, density, shape_factor]
data = [
    [0.3, 20, 3, 500, 1],   # screwdriver
    [0.5, 10, 10, 300, 2],  # ball
    [1.2, 25, 20, 700, 3],  # box
    [0.4, 22, 4, 520, 1],   # screwdriver
    [0.6, 11, 11, 310, 2],  # ball
    [1.1, 24, 18, 680, 3]   # box
]

# Labels:
# 0 = screwdriver
# 1 = ball
# 2 = box
labels = [0, 1, 2, 0, 1, 2]

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=20, random_state=42)
model.fit(data, labels)

# ============================================================
# Test Input (example)
# ============================================================

# Replace this with real sensor data when available
test_input = [[0.55, 12, 10, 320, 2]]

prediction = model.predict(test_input)[0]

# Map numeric label back to object name
object_names = {0: "screwdriver", 1: "ball", 2: "box"}
predicted_object = object_names[prediction]

print("Predicted Object:", predicted_object)

# Training accuracy
accuracy = model.score(data, labels)
print("Training Accuracy:", accuracy)
