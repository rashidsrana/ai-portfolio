# # Research Methodology


# ### Titanic dataset


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print(plt.style.available)


plt.style.use(style="petroff10")
plt.rcParams["figure.figsize"] = (10, 8)
# try other options like colors and fonts


# # Load and explore the dataset


titanic = pd.read_csv(r"titanic.csv")


titanic


titanic.head(10)


# # Research question:
# - Average age
# - number of males and females
# - count of each class
# - avg fare prices for each class
# - survived / not survived
# - survivals-gender
# - survivals-class
# - survivals-age
# - sarvivals-sib/parch


titanic.shape


titanic.tail(10)


titanic.info()


titanic.describe()


titanic.describe().all()


titanic.isnull()


titanic.isnull().sum()


titanic.duplicated().sum()


titanic.describe(include="all").T


titanic.columns


titanic.nunique()


titanic.Pclass.describe()


titanic["Pclass"].info()


titanic["Pclass"].isnull().sum()


titanic["Pclass"].nunique()


titanic.select_dtypes(include=["object"]).describe().T


titanic.select_dtypes(include=["object"]).T


titanic.describe(include=["object"]).T


titanic.describe(include=["float"]).T


sns.pairplot(titanic, hue="Survived")
plt.show()


corr_matrix = titanic.corr(numeric_only=True)
corr_matrix


sns.heatmap(corr_matrix, annot=True)
plt.title("correlation matrix for titanic dataset")
plt.show()


# ## Cleaning the dataset


# dropping the columns not needed in the analysis
titanic.drop(["Lname", "Name", "Ticket", "Fare", "Cabin"], axis=1, inplace=True)


titanic.head()


titanic["Age"].mean().round(2)


avg = titanic["Age"].median()


titanic["Age"] = titanic["Age"].fillna(avg)


mod = titanic["Embarked"].mode()
mod


titanic["Embarked"] = titanic["Embarked"].fillna("s")


titanic.isnull().sum()


# ### Analysis and Visualization


# #### 1. Percentage of Survival


# No. of people survived vs Not survived
survival = titanic["Survived"].value_counts()
survival


# pie chart for survival


plt.pie(survival, labels=["did not survive", "survived"], autopct="%1.1f%%")
plt.title("Titanic Survival Percentage")
plt.show()


# ### Survivors by Gender


gender_count = titanic["Sex"].value_counts()
gender_count


survivor_gender = titanic[["Sex", "Survived"]].groupby("Survived").count()
survivor_gender


survivor_gender = titanic[["Sex", "Survived"]].groupby("Sex").count()
survivor_gender


survivor_gender_ct = pd.crosstab(titanic["Survived"], titanic["Sex"])
survivor_gender_ct


survivor_gender_ct_per = (
    pd.crosstab(titanic["Survived"], titanic["Sex"], normalize="columns").round(2) * 100
)
survivor_gender_ct_per


survivor_gender_ct_per.plot(kind="bar")
plt.show()


survivor_gender_ct_per.T.plot(kind="bar", rot=0)
plt.show()


# ###
