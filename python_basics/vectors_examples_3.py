
# # Task 1: NumPy Vectors and Matplotlib Plots


import numpy as np
import matplotlib.pyplot as plt


vector_a=np.array([11,17,25])
print(vector_a)


vector_b=np.array([5,4,3])
print(vector_b)


print(f"Sum of vector_a and vector_b is {np.add(vector_a,vector_b)}")
print(f"Subtract vector_b from vector_a is {np.subtract(vector_a,vector_b)}")
print(f"the product of the two vectors is {np.multiply(vector_a,vector_b)}")
print(f"Mean of vector_a is {np.mean(vector_a)}")
print(f"Mean of vector_a is {np.mean(vector_b)}")
print(f"std of vector_a is {np.std(vector_a)}")
print(f"std of vector_a is {np.std(vector_b)}")



# # Task 2: Plotting with Matplotlib



vectors = [vector_a, vector_b]
labels = ['vector_a', 'vector_b']
colors = ['green', 'yellow']

# -----------------------------
# 1. Plot the vectors in 2D
# -----------------------------
plt.figure(figsize=(8, 6))
origin = np.zeros(2)

for vec, label, c in zip(vectors, labels, colors):
    plt.quiver(
        *origin, *vec,
        angles='xy',
        scale_units='xy',
        scale=1,
        color=c,
        edgecolor=c,
        linewidth=2,
        label=label
    )

plt.xlim(0, max(vector_a[0], vector_b[0]) + 1)
plt.ylim(0, max(vector_a[1], vector_b[1]) + 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2D Vector Plot")
plt.grid(True)
plt.legend()
plt.show()

# -----------------------------
# 2. Bar plot of mean values
# -----------------------------
means = [v.mean() for v in vectors]

plt.figure(figsize=(8, 6))
plt.bar(labels, means, color=colors)
plt.title("Mean of Each Vector")
plt.ylabel("Mean Value")
plt.show()

# -----------------------------
# 3. Bar plot of standard deviations
# -----------------------------
stds = [v.std() for v in vectors]

plt.figure(figsize=(8, 6))
plt.bar(labels, stds, color=['green', 'yellow'])
plt.title("Standard Deviation of Each Vector")
plt.ylabel("Standard Deviation")
plt.show()



