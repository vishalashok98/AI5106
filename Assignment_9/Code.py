import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import inv
from numpy import linalg as LA
from numpy import zeros
from numpy import diag
from numpy import dot
m1 = np.array(([1,0,0.5]))
m2 = np.array(([0,1,0.75]))
A = np.vstack((m1,m2)).T
b=np.array([-2,1,1.5])
Dv, Pv=LA.eig(A.T.dot(A))
Du, Pu=LA.eig(A.dot(A.T))
Stemp=np.sqrt(Dv)
V, Rv=LA.qr(Pv)
U, Ru=LA.qr(Pu)
U_1, s, V_1=LA.svd(A)
Sigma = zeros((A.shape[0], A.shape[1]))
Sigma[:A.shape[1], :A.shape[1]] = diag(s)
B = U.dot(Sigma.dot(V_1))
print('Eigen vector matrix of Mtranspose*M',V)
print('V',V_1)
print('Eigen vector matrix of M*Mtranspose',U)
print('U',U_1)
print('Sigma matrix of SVD',s)
print(Stemp)
print(B)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.plot3D([-1], [2], [4], marker='o', label='P = (-1, 2, 4)')
ax.text(-1, 2, 4,'P')
ax.plot3D([3, -1], [8,2], [-4, 4], color='b')
xx, yy = np.meshgrid([-10,30], range(6)) 
n1 = np.array([2,3,-4]).reshape((3,1))
A =  np.array([-1,2,4]).reshape((3,1))
c1 = 5
z1 = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])
Plane=ax.plot_surface(xx, yy, z1,label='Plane', color='r',alpha=0.5)
Plane._facecolors2d=Plane._facecolors3d
Plane._edgecolors2d=Plane._edgecolors3d
plt.legend(loc='best')
plt.show()
