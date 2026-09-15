# # Dataframes in Pandas


# - A dataframe in pandas is a 2D structure like table with rows and columns.
# - It is very popular in Data Science for analyzing Datasets.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {"name": ["alex", "brianna"], "city": ["Caledon", "Milton"], "age": [78, 45]}
print(data)


df = pd.DataFrame(data)
print(df)


df


print(df["name"])


print(df[["name", "city"]])


# first row
df.iloc[0]


# row 0, 1
df.iloc[0:2]


# first column
df.iloc[:, 0]


df.loc[:, "age"]


df.loc[:, ["name", "age"]]


# add a new column
df["salary"] = [60000, 90000]


df


# add a new row
df.loc[2] = ["Nic", "Hamilton", 34, 85000]
df


# change existing value
# age 78 to 58
df.at[0, "age"] = 58
df


# rows and columns
df.shape


# min, max, mean, median, sum, std on age
# df['age'].mean()
df.age.mean()


df["age"].median()


df["age"].sum()


df["age"].min()


df["age"].max()


df["age"].std()


# drop columns
df.drop("salary", axis=1)
# df.drop(df.columns[1],axis=1)


df


# dropping row/(s)
df.drop([1, 2])


# correlation
# -1 to 1
corr_age_sal = df["age"].corr(df["salary"])
corr_age_sal


data1 = {"name": ["alex", "brianna"], "city": ["Caledon", np.nan], "age": [78, np.nan]}
print(data1)


df1 = pd.DataFrame(data1)
df1


# dropna
df1.dropna()


df1


# fillna
df1 = df1.fillna({"age": df1["age"].mean(), "city": "Milton"})
# df1.fillna({'age':df1['age'].mean(),'city':'Milton'},inplace=True)
df1


df1


dataFromCSV = pd.read_csv(r"iris.csv")


dataFromCSV.head()


num_rows = len(dataFromCSV)
print(f"Number of rows: {num_rows}")
numb_rows_10 = dataFromCSV.head(10)
numb_rows_10


dataFromCSV.iloc[:10]


dataFromCSV.info()
dataFromCSV.describe()


dataFromCSV.isnull()
dataFromCSV.isna()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"Mall_Customers.csv")
df = pd.DataFrame(data)
print(df)
first10Rows = df.head(10)
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
data.info()
data.describe()

# Count missing values per column
missing_per_column = df.isnull().sum()
print("Missing values per column:")
print(missing_per_column)

# Example: Female customers, age < 30, and spending score > 70
filtered_customers = df[
    (df["Genre"] == "Female") & (df["Age"] < 30) & (df["Spending Score (1-100)"] > 70)
]

# 3. View the results
print(filtered_customers)

# 1. Define High-Spending (e.g., > 90)
high_spend_threshold = 80
high_spenders = df[df["Spending Score (1-100)"] > high_spend_threshold]

# 2. Count high-spenders
count = len(high_spenders)
print(f"High-spending customers: {count}")

# 3. Calculate gender percentages among high-spenders
percentages = high_spenders["Genre"].value_counts(normalize=True) * 100
print(percentages)

df["Income per Age"] = df["Annual Income (k$)"] / df["Age"]

# print(df)

# 3. Compute its average
average_ipa = df["Income per Age"].mean()

print(df)
print(f"\nAverage Income_per_Age: {average_ipa}")


# Create the histogram
df["Age"].hist(bins=10)  # You can adjust the number of bins
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


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


# Calculate and plot in one go
df.groupby("Genre")["Spending Score (1-100)"].mean().plot(
    kind="bar", color=["skyblue", "salmon"]
)
plt.title("Average Spending Score by Gender")
plt.ylabel("Average Spending Score")
plt.xticks(rotation=0)
plt.show()


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
