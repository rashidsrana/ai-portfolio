# Single variable Linear Regression on Iris Dataset

import pandas as pd

# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error,r2_score

# import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data=pd.read_csv("iris.csv")
df = pd.read_csv(r"iris.csv")
# print(df)

df.head(10)

df.tail(10)

df.shape

df.describe()

df.describe(include="all")

df.info()

df.isnull().sum()

corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation matrix for IRIS dataset")
plt.show()
