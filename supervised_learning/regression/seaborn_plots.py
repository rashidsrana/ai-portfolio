import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)
# iris

print(iris.head())

print(iris.tail())

print(iris.info())

print(iris.describe())

iris.describe(include="all")

print(iris.shape)

iris.isnull().sum()

iris.duplicated().sum()

sns.set(style="darkgrid", palette="bright", context="notebook")

sns.pairplot(iris, hue="species", markers=[".", "d", "*"])
plt.show()

sns.boxplot(x="species", y="sepal_length", data=iris)
plt.show()

sns.boxplot(x="species", y="petal_length", data=iris)
plt.show()

sns.boxplot(x="species", y="petal_width", data=iris)
plt.show()


sns.scatterplot(x="petal_length", y="petal_width", hue="Species", data=iris)
plt.title("Scatterplot for petal_length and petal_width")
plt.show()

corr = iris.corr(numeric_only=True)
corr

sns.heatmap(corr, annot=True, cmap="inferno")
plt.show()

sns.barplot(x="species", y="petal_length", data=iris)
plt.show()

sns.countplot(x="species", data=iris)
plt.show()

sns.swarmplot(x="species", y="petal_width", data=iris, palette="inferno")
plt.show()
