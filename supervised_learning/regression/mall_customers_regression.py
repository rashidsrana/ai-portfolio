#   Panadas & Matplotlib

# 1. Setup & Load Data

# Import pandas, numpy, and matplotlib.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Mall_Customers.csv into a DataFrame.
data = pd.read_csv(r"Mall_Customers.csv")
df = pd.DataFrame(data)
print(df)

# Show first 10 rows and check dataset shape
first10Rows = df.head(10)

# check dataset shape
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")


# 2. Basic Exploration

# Use info() and describe() to inspect data.
data.info()
data.describe()

# Count missing values per column
missing_per_column = df.isnull().sum()
print("Missing values per column:")
print(missing_per_column)

# 3. Data Manipulation
# Filter customers by gender, age, and spending score
# Example: Female customers, age < 30, and spending score > 70
filtered_customers = df[
    (df["Genre"] == "Female") & (df["Age"] < 30) & (df["Spending Score (1-100)"] > 70)
]

# 3. View the results
print(filtered_customers)

# Count high spending customers and calculate gender percentages.
# 1. Define High-Spending (e.g., > 90)
high_spend_threshold = 80
high_spenders = df[df["Spending Score (1-100)"] > high_spend_threshold]

# 2. Count high-spenders
count = len(high_spenders)
print(f"High-spending customers: {count}")

# 3. Calculate gender percentages among high-spenders
percentages = high_spenders["Genre"].value_counts(normalize=True) * 100
print(percentages)
# Create a new column: Income_per_Age.
df["Income per Age"] = df["Annual Income (k$)"] / df["Age"]

# 3. Compute its average
average_ipa = df["Income per Age"].mean()

print(df)
print(f"\nAverage Income_per_Age: {average_ipa}")


# 4. Visualizations

# Create the histogram
df["Age"].hist(bins=10)  # You can adjust the number of bins
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Scatter plot: Annual Income vs. Spending Score.
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x="Annual Income (k$)", y="Spending Score (1-100)", hue="Genre", s=100
)  # s controls dot size

plt.title("Scatter Plot: Annual Income vs. Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# Bar chart: Average Spending Score by Gender.
df.groupby("Genre")["Spending Score (1-100)"].mean().plot(
    kind="bar", color=["skyblue", "salmon"]
)
plt.title("Average Spending Score by Gender")
plt.ylabel("Average Spending Score")
plt.xticks(rotation=0)
plt.show()

# Boxplot: Spending Score by Gender.

# 1. Separate the Spending Scores by Gender
male_scores = df.loc[df["Genre"] == "Male", "Spending Score (1-100)"]
female_scores = df.loc[df["Genre"] == "Female", "Spending Score (1-100)"]

# 2. Group the data lists together for the boxplot function
plot_data = [male_scores, female_scores]

# 3. Create the box plot using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))  # Create a figure and axes object

# Pass the list of data arrays to the boxplot function
ax.boxplot(plot_data, patch_artist=True)

# 4. Customize the plot with titles and labels
ax.set_title("Boxplot: Spending Score by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Spending Score (1-100)")
ax.set_xticklabels(["Male", "Female"])  # Set the custom x-axis labels
plt.grid(True, axis="y")  # Add grid lines for better readability

# 5. Display the plot
plt.show()
