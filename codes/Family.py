#Family of lines passing through a point

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg 
 
P = np.array([[4,3],
              [3,4]])#Coefficients of x,y in both equations
Q = np.array([[12],
               [12]])#constants in both equations
               
          
Pin = linalg.inv(P)#Finding inverse of P
I = np.matmul(Pin,Q)#Finding the intersection point
print I
X = np.linspace(-1,3,2)
#Z = np.zeoros(50)

m = np.linspace(-10,10,20)
Y = np.zeros((20,2))


for i in range(20):
   for j in range(2):
     Y[i,j] = m[i]*(X[j]-I[0]) + I[1]
   plt.plot(X[:],Y[i,:])

plt.plot(I[0],I[1], 'o')
plt.text(I[0]*(1),I[1]*(1+0.4),'I')
plt.grid()
plt.show()
