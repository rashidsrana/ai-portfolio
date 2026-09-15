# # WHO Global Health Dataset analysis


import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(
    r"LinearRegression\World Health Org Global Health data set Pivot Tables (2).xlsx",
    sheet_name="Global Health Statistics 2012",
)
df


df.head(10)


df.tail(10)


df.info()


df.describe().T


df.describe(include="all").T


df.isnull().sum()


df.duplicated().sum()


df.shape


df.columns


df.nunique()


sns.pairplot(df, hue="economic status")
plt.show()


corr_matrix = df.corr(numeric_only=True)
corr_matrix


sns.heatmap(corr_matrix, annot=True)
plt.show()


# # Research questions
# 1. average pcgovhealth based on economic status
# 2. food safety based on economic status
# 3. average life based on economic status
# 4. average life of a male vs female based on economic status
# 5. average bithrate based on economic status
# 6. average life based on food safety risk level and govt spending level


# <img src="rq.png">


# # Analysis


# ## 1. average pcgovhealth based on economic status


eco_pc = df.groupby("economic status")["pcgovhealth"].mean()
eco_pc


px.bar(
    eco_pc, y="pcgovhealth", title="Average govt spending based on economic status"
).show()


# ## 2. food safety based on economic status


df.groupby("economic status")["foodsafety"].mean().round(2)


# add plot


# ## 3. average life based on economic status


eco_life = df.groupby("economic status")["lifebirth"].mean().round(0)
eco_life


px.bar(eco_life, y="lifebirth", title="Average life on economic status").show()


# # 4. average life of a male vs female based on economic status


compare_age = (
    df.groupby("economic status")[["lifebirth", "mlifebirth", "flifebirth"]]
    .mean()
    .round(0)
)
compare_age


# create a plot
# paste screenshots in chat
px.bar(compare_age, title="Average age comparison").show()


fig = px.bar(compare_age, title="Average age comparison")
fig.update_layout(barmode="group")
fig.show()


# ## 5. average bithrate based on economic status


# add analysis


# Add plot


# ## 6. average life based on food safety risk level and govt spending level


df.groupby(["foodsafety risk level", "gov spending level"])["lifebirth"].mean().round(0)


pd.crosstab(
    df["foodsafety risk level"],
    df["gov spending level"],
    values=df["lifebirth"],
    aggfunc="mean",
).fillna(0)


# add plot


# # Summary of Findings


# 1. it is found that the average govt spending in  DC : 3083$, LDC : 292$ and LLDC : 60$.
# 2. **complete the findings**
#
