import numpy as np
import matplotlib.pyplot as plt

#finding the coeffecients
x = np.array([2, 5, 7, 10, 14, 17, 22, 26, 29, 34, 37, 41, 44, 48, 51, 53, 57, 61, 65, 68, 71, 74, 76, 79, 82, 85, 87, 90, 94, 98])
y = np.array([2, 7, 5, 2,1,11,13,28,22, 4, 4, 7, 9, 3, 12, 6, 8, 2, 5, 14, 10, 1, 13, 17, 15, 16, 18, 0, 19, 14])
n = len(x)
h = np.diff(x)
b = np.zeros(4*n-4)
b[0]=y[0]
iter_1=1
iter_2=1
for i in range(n-2):
    b[iter_1] = y[iter_2]
    b[iter_1+1] = y[iter_2]
    iter_1 = iter_1 + 2
    iter_2 = iter_2 + 1
b[iter_1] = y[iter_2]
b = b[:, np.newaxis]
A = np.zeros((4*n-4,4*n-4))
iter_3=0
iter_4=3
iter_5=0
#basically putting values of constants attached w coeffecients in the a matrix on their respective indexes
for i in range(n-1):
    A[iter_3][iter_4] = 1
    A[iter_3+1][iter_4-3] = h[iter_5]**3
    A[iter_3+1][iter_4-2] = h[iter_5]**2
    A[iter_3+1][iter_4-1] = h[iter_5]
    A[iter_3+1][iter_4] = 1
    iter_3 = iter_3 + 2
    iter_4 = iter_4 + 4
    iter_5 = iter_5 +1
iter_3 = 2*n-2
iter_4 = 0
iter_5 = 0
for i in range(n-2):
    A[iter_3][iter_4] = 3*h[iter_5]**2
    A[iter_3][iter_4+1] = 2*h[iter_5]
    A[iter_3][iter_4+2] = 1
    A[iter_3][iter_4+6] = -1
    A[iter_3+1][iter_4] = 6*h[iter_5]
    A[iter_3+1][iter_4+1] = 2
    A[iter_3+1][iter_4+5] = -2
    iter_3 = iter_3+2
    iter_4 = iter_4+4
    iter_5 = iter_5+1
A[iter_3][1] =2
A[iter_3+1][iter_4] = 6*h[iter_5]
A[iter_3+1][iter_4+1] = 2
c = np.dot(np.linalg.inv(A), b)
l = 0
m = 0
plt.figure(figsize=(35,5))
for i in range(n-1):
    def S(X):
        return c[l]*(X-x[m])**3+c[l+1]*(X-x[m])**2+c[l+2]*(X-x[m])+c[l+3]
    x_values = np.linspace(x[m],x[m+1],100)
    plt.plot(x_values, S(x_values), )
    l=l+4
    m=m+1
plt.title('Cubic Spline Interpolation for n points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()









