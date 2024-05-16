import numpy as np
import matplotlib.pyplot as plt


def curv(x1, y1):
    # finding the coeffecients
    x = np.array([1, 2, 3, 4])
    y = np.array([2, 4, 1, 9])
    h = np.array([x[1] - x[0], x[2] - x[1], x[3] - x[2]])
    b = np.array([y[0], y[1], y[1], y[2], y[2], y[3], 0, 0, 0, 0, float(x1), float(y1)])
    b = b[:, np.newaxis]
    A = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [h[0] ** 3, h[0] ** 2, h[0], 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, h[1] ** 3, h[1] ** 2, h[1], 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, h[2] ** 3, h[2] ** 2, h[2], 1],
                  [3 * h[0] ** 2, 2 * h[0], 1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
                  [6 * h[0], 2, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 3 * h[1] ** 2, 2 * h[1], 1, 0, 0, 0, -1, 0],
                  [0, 0, 0, 0, 6 * h[1], 2, 0, 0, 0, -2, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 6 * h[2], 2, 0, 0]])
    c = np.dot(np.linalg.inv(A), b)

    def dS_0(X):
        return 3 * c[0] * (X - x[0]) ** 2 + 2 * c[1] * (X - x[0]) + c[2]

    def ddS_0(X):
        return 6 * c[0] * (X - x[0]) + 2 * c[1]

    def dS_1(X):
        return 3 * c[4] * (X - x[1]) ** 2 + 2 * c[5] * (X - x[1]) + c[6]

    def ddS_1(X):
        return 6 * c[4] * (X - x[1]) + 2 * c[5]

    def dS_2(X):
        return 3 * c[8] * (X - x[2]) ** 2 + 2 * c[9] * (X - x[2]) + c[10]

    def ddS_2(X):
        return 6 * c[8] * (X - x[2]) + 2 * c[9]

    return ddS_0(x[0])**2/(1+dS_0(x[0])**2)**3 + ddS_0(x[1])**2/(1+dS_0(x[1])**2)**3 + ddS_1(x[2])**2/(1+dS_2(x[2])**2)**3 + ddS_2(x[3])**2/(1+dS_2(x[3])**2)**3

# Finite difference approximation of gradient
def gradient_approximation(x1, y1, h=1e-5):
    grad_x = (curv(x1 + h, y1) - curv(x1, y1)) / h
    grad_y = (curv(x1, y1 + h) - curv(x1, y1)) / h
    return grad_x, grad_y


# Gradient Descent Optimization function
def gradient_descent(initial_x, initial_y, learning_rate, iterations):
    x1 = initial_x
    y1 = initial_y

    for i in range(iterations):
        grad_x, grad_y = gradient_approximation(x1, y1)
        x1 -= learning_rate * grad_x
        y1 -= learning_rate * grad_y

    return x1, y1

# Initial values and hyperparameters
initial_x = 0
initial_y = 0
learning_rate = 0.1
iterations = 100000

# Run gradient descent
optimal_x, optimal_y = gradient_descent(initial_x, initial_y, learning_rate, iterations)

print("Optimal x:", optimal_x)
print("Optimal y:", optimal_y)
print("Optimal function value:", curv(optimal_x, optimal_y))

