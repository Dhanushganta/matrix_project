import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg 
 
P = np.array([[4,3],
              [3,4]])#Coefficients of x,y in both equations
Q = np.array([[12],
               [12]])#constants in both equations
               
          
Pin = linalg.inv(P)#Finding inverse of P
I = np.matmul(Pin,Q)#From property 
print I

R = 501
m = np.linspace(-20,20,R)#Parameter
#Creating arrays of variable sizes

d = np.zeros(R)
e = np.zeros(R)
s = np.zeros((R,2))
X = np.zeros((R,2))
A = np.zeros(R)
B = np.zeros(R)
t = np.zeros(R)

for i in range (R):
    d[i] = (12-4*m[i])/3#In the given equation 4x+3y=12 by substituting m[i] in x and entering values of y into an array d
    e[i] = (12-3*m[i])/4#In the given equation 3x+4y=12 by substituting m[i] in x and entering values of y into an array e
    s[i,:] = np.array([m[i],-1])#Entering the values of (m[i],-1) into each row of 2XR sized matrix 
    A[i] = (np.matmul(s[i,:],I))/m[i]#Calculating the points at which the family of lines meet the x-axis and entering them in an array 'A'
    B[i] = -(np.matmul(s[i,:],I))#Calculating the points at which the family of lines meet the y-axis and entering them in an array 'B'
    X[i,:] = np.array([A[i]/2,B[i]/2])#Entering the midpoints of A and B into a new array 'X' of size RX2


plt.plot(m[:],d[:],label='$d$') #Ploting the line 'd'
plt.plot(m[:],e[:],label='$e$') #Ploting the line 'e'
plt.plot(I[0],I[1], 'o')#Ploting 
plt.text(I[0]*(1+0.5),I[1]*(1+0.5),'I')
plt.plot(X[:,0],X[:,1],label='$Locus of midpoint$') #Ploting the locus of midpoints of A and B
plt.plot(m[:],t[:],label='$X-Axis$')
plt.plot(t[:],m[:],label='$Y-Axis$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.show()



