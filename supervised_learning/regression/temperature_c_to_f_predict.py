import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Dataset
# Celsius values
X = np.array([[0], [10], [20], [30], [40]], dtype=float)

# Fahrenheit values
y = np.array([[32], [50], [68], [86], [104]], dtype=float)

# 2. Build the model
model = Sequential([
    Dense(16, activation='relu', input_shape=(1,)),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# 3. Train the model
model.fit(X, y, epochs=500, verbose=0)

# 4. Predict for a new Celsius value
new_celsius = 25
prediction = model.predict(np.array([[new_celsius]]))

print("Input Celsius:", new_celsius)
print("Predicted Fahrenheit:", prediction[0][0])
