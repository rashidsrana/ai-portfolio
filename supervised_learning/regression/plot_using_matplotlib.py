
# Scatter Plot

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,14,5,16]
plt.figure(figsize=(8,5))
plt.scatter(x,y,color="blue",marker="^",s=90,edgecolor="red")
plt.title("scatter plot",fontsize=18,color="green")
plt.xlabel('X-axis',fontsize=6)
plt.ylabel('Y-axis',fontsize=6)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()


# Line Plot
plt.figure(figsize=(8,5))
plt.title("Line plot",fontsize=18,color="red")
plt.xlabel('X-axis',fontsize=9)
plt.ylabel('Y-axis',fontsize=9)
plt.grid(True,linestyle="--",alpha=0.5)

plt.plot(x,y,color="red",marker="o",linestyle="--")
plt.show()

# Bar Plot
A=['gloves','tshirt','shoes','glasses']
B=[20,25,58,15]
plt.figure(figsize=(8,5))
plt.title("Bar plot",fontsize=18,color="red")
plt.xlabel('X-axis',fontsize=9)
plt.ylabel('Y-axis',fontsize=9)
plt.grid(True,linestyle="--",alpha=0.5)
plt.bar(A,B,color="green")
plt.show()

# Pie Chart
colors=['pink','green','yellow','blue']
plt.pie(B,labels=A,autopct='%1.1f%%', colors=colors,shadow=True)
plt.title("pie chart",fontsize=18,color="blue")
plt.show()


# Histogram
data=[1,2,2,3,3,3,4,4,4,4,4,4,4]
plt.hist(data)
plt.show()