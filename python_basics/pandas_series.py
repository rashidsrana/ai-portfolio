
# # Series 


data=[3,5,7,"abc",True,3.14]
print(data)


import pandas as pd


series1 = pd.Series(data)
print(series1)


import matplotlib.pyplot as plt
data2=[2,4,6,8,20,40]
series2=(data2)
plt.plot(series2)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

data2=[2,4,6,8,20,40]

series2 = pd.Series(data2)
plt.bar(series2.index,series2.values)
plt.show()





labels=["L1","L2","L3","L4","L5"]
data=[11,33,55,22,33]

series2 = pd.Series(data,index=labels)


print(series2.mean())
print(series2.median())
print(series2.sum())
print(series2.std())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name':['alex', 'bianca'], 'city':['Toronto', 'London'], 'age':[34,43]}
print(data)


df=pd.DataFrame(data)
print(df)


df


data


df.index





