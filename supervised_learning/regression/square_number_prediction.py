# run following commads in terminal, switch 3.14 to 3.11
# Install following libraries
# python -m pip install numpy
# changed python verison from 3.14 to 3.11 for compatible tensorflow
# python -m pip install tensorflow
# py -3.11 -m venv tf-env
# tf-env\Scripts\activate
# run this file in terminal using command "py squareNumberPredict.py", not from play icon, as play icon uses 3.14




import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# ---------------------------------------------------------
# 1. Create dataset
# ---------------------------------------------------------
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]], dtype=float)
#y = np.array([[1], [4], [9], [16], [25],[36],[49],[64],[81]], dtype=float)
y = X ** 2

# ---------------------------------------------------------
# 2. Build a simple neural network
# ---------------------------------------------------------
model = Sequential([
    Input(shape=(1,)),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# ---------------------------------------------------------
# 3. Train the model
# ---------------------------------------------------------
model.fit(X, y, epochs=1000, verbose=0)

# ---------------------------------------------------------
# 4. Predict the square of a new number
# ---------------------------------------------------------
test_value = np.array([[6]])   # should predict 36
prediction = model.predict(test_value)

print("Input:", test_value[0][0])
print("Predicted square:", prediction[0][0])
