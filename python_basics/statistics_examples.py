
import statistics as st


x = [1,2,2,4,6,8,9]
print(st.mean(x))


y = st.median(x)
y


st.stdev(x)


st.variance(x)


st.mode(x)


round(st.mean(x), 2)



round(st.variance(x),2)


round(st.stdev(x),2)


print(f"The variance is = {st.variance(x)}:.2f")


x1 = [1,2,2,4,4,6,8,9,10]
st.multimode(x1)


x2=[1,3,5,7]
st.median_low(x2)


st.median_high(x2)


st.median(x2)


st.geometric_mean(x2)


st.harmonic_mean(x2)


st.fmean(x2)


st.quantiles(x1,n=3)


st.quantiles(x1,n=4)


# divide data into 10 start



st.quantiles(x1,n=10)


st.quantiles(x1,n=8)


data=[1,2,2,3,4,5,5,5,6]


print(st.mean(data))
print(st.median(data))
print(st.mode(data))


import matplotlib.pyplot as plt
plt.hist(data,bins=range(1,8),edgecolor="yellow",color="blue")
plt.axvline(st.mean(data),color="r",label=f"mean is:{st.mean(data):2f}", linestyle="dashed")
plt.axvline(st.median(data),color="b",label=f"median is:{st.median(data):2f}", linestyle="dashed")
plt.axvline(st.mode(data),color="g",label=f"mode is:{st.mode(data):2f}", linestyle="dashed")
plt.legend()
plt.title("Histogram for measures of central tendency",color="red")
plt.ylabel("frequency")
plt.xlabel("value")
plt.show()

  # VECTORS

  ### vectors
# - A vector is a mathematical object that has a magnitude (length) and direction.
# - Vector ara used in engineering, physics, math,ML,DL.
# - Vector can be represented using an arrow with tail and head (starting and ending point)
# 
# # Vectors in python   
# 
# . A vector in python is an ordered collection of nombers.
# . Represeneted using lists,tuples and more often using Numpy arrays.
# 
# # Operations on Vectors
# 


import numpy as np
import matplotlib.pyplot as plt



vector1=np.array([1,2,3])
print(vector1)


np.mean(vector1)


np.median(vector1)


np.sum(vector1)


np.std(vector1)


np.var(vector1)


np.min(vector1)


np.max(vector1)


np.percentile(vector1,75)


vector2 = np.array([3,4,5])
vector2


sum_vec = vector1 + vector2
sum_vec


from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.quiver(0,0,0, vector1[0], vector1[1], vector1[2],label="vector 1",color="blue",linestyle="dashed")
ax.quiver(0,0,0, vector2[0], vector2[1], vector2[2],label="vector 2",color="red")
ax.quiver(0,0,0, sum_vec[0],sum_vec[1],sum_vec[2],label="sum_vec",color="green",linestyle="dotted")
ax.set_xlim([0,10])
ax.set_ylim([0,10])
ax.set_zlim([0,10])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.legend()
plt.show()


vector1_mean=np.mean(vector1)
vector2_mean=np.mean(vector2)
sum_vec_mean=np.mean(sum_vec)


labels = ['mean_vector1', 'mean_vector2', 'mean_sum']
means = [vector1_mean, vector2_mean, sum_vec_mean]
colors = ['red', 'blue', 'green']

plt.figure(figsize=(8,5))
plt.bar(labels, means, color=colors, label=labels)
plt.title("Mean of Vectors")
plt.ylabel("mean_values")
plt.xlabel("Vectors")
plt.legend(labels)
plt.grid(True)
plt.show()





sub_vec=vector2-vector1
sub_vec


#scalar multiplication
vector1*4


dot_prod=np.dot(vector1,vector2)
dot_prod


cr_prod=np.cross(vector1,vector2)
cr_prod


# magnitude
mag=np.linalg.norm(vector1)
mag


# normalization
nor_vec=vector1/mag
nor_vec





