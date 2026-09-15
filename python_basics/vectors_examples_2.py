
import numpy as np
import matplotlib.pyplot as plt

# Example vectors (replace with your own)
vector_a=np.array([11,17,25])
vector_b=np.array([5,4,3])

vectors = [vector_a, vector_b]
labels = ['v1', 'v2']

# -----------------------------
# 1. Plot the vectors in 2D
# -----------------------------

plt.figure(figsize=(6, 6))
origin = np.zeros(2)

colors = ['red', 'green']   # your custom colors

for vec, label, c in zip(vectors, labels, colors):
    plt.quiver(
        *origin, *vec,
        angles='xy',
        scale_units='xy',
        scale=1,
        color=c,          # color of arrow fill
        edgecolor=c,      # color of arrow outline (important!)
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


plt.figure(figsize=(6, 6))
origin = np.zeros(2)



# -----------------------------
# 2. Bar plot of mean values
# -----------------------------
means = [v.mean() for v in vectors]

plt.figure(figsize=(6, 4))
plt.bar(labels, means, color=['blue', 'orange'])
plt.title("Mean of Each Vector")
plt.ylabel("Mean Value")
plt.show()

# -----------------------------
# 3. Bar plot of standard deviations
# -----------------------------
stds = [v.std() for v in vectors]

plt.figure(figsize=(6, 4))
plt.bar(labels, stds, color=['blue', 'orange'])
plt.title("Standard Deviation of Each Vector")
plt.ylabel("Standard Deviation")
plt.show()





