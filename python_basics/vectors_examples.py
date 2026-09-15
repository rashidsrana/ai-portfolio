
# # VECTORS


# ### Vectors
# - A vector is a mathematical object that has a magnitude (length) and direction.
# - Vectors are used in engineering, physics, maths, ML,DL.
# - Vector can be represented using an arrow with tail and head (starting and ending point)


# ### Vectors in Python
# - A vector in Python is an ordered collection of numbers.
# - Represented using lists, tuples and more often using Numpy arrays.


# # Operations on Vectors


import numpy as np
import matplotlib.pyplot as plt


vector1=np.array([1,2,3])
print(vector1)


np.mean(vector1)


vector1.mean()


# median,mode, sum,std,var,min,max,percentile,quantile
print(np.median(vector1))
print(np.sum(vector1))
print(np.std(vector1))
print(np.var(vector1))
print(np.min(vector1))
print(np.max(vector1))
print(np.percentile(vector1,75))
print(np.quantile(vector1,.75))


vector2=np.array([3,4,5])
vector2


sum_vec=vector1+vector2
sum_vec


from mpl_toolkits.mplot3d import Axes3D


fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.quiver(0,0,0,vector1[0],vector1[1],vector1[2],label="Vector 1",color="red")
ax.quiver(0,0,0,vector2[0],vector2[1],vector2[2],label="Vector 2",color="green")
ax.quiver(0,0,0,sum_vec[0],sum_vec[1],sum_vec[2],label="Sum Vector",color="blue")
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
vectorsum_mean=np.mean(sum_vec)


# <img src="download.png">


mean_vec=[vector1_mean,vector2_mean,vectorsum_mean]


plt.bar(["vector1_mean","vector2_mean","vectorsum_mean"],mean_vec,color=["yellow","brown","purple"],label=["vector1_mean","vector2_mean","vectorsum_mean"])
plt.xlabel("Vectors")
plt.ylabel("mean values")
plt.title("Mean of Vectors")
plt.legend()
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





