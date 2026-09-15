
# <h1 style="color:white;background-color:gray;padding:10px"> Getting started with Matplotlib</h1>


# **Matplotlib** is python's main plotting and visualization library.
# Some common plots include:
# - line plots
# - scatter plots
# - bar charts
# - histograms
# - pie charts
# - heatmaps
# - subplots


# # Scatter plots


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,14,5,16]
plt.figure(figsize=(8,5))
plt.scatter(x,y,color="green",marker="^",s=90,edgecolor="red")
plt.title("Scatter Plot",fontsize=18,color="green")
plt.xlabel('X-axis',fontsize=8)
plt.ylabel('Y-axis',fontsize=8)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()


# # Line plots


plt.plot(x,y)
plt.show()


plt.figure(figsize=(8,5))
plt.plot(x,y,color="green",marker="o",linestyle="--",markersize=10)
plt.title("Line Plot",fontsize=18,color="green")
plt.xlabel('X-axis',fontsize=8)
plt.ylabel('Y-axis',fontsize=8)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()


# # Bar Plot


A=['gloves','tshirt','shoes','glasses']
B=[18,45,78,34]
plt.bar(A,B,color="green")
plt.title("Bar Plot",fontsize=18,color="green")
plt.xlabel('Products',fontsize=8)
plt.ylabel('sales',fontsize=8)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()


# # Pie Chart


colors=['red','green','blue','pink']
plt.pie(B,labels=A,autopct='%1.1f%%',colors=colors,shadow=True)
plt.title("Pie Chart",fontsize=18,color="green")
plt.tight_layout()
plt.show()


# # Histogram


data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data)
plt.show()





