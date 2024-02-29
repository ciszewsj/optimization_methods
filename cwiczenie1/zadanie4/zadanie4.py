import os

import matplotlib.pyplot as plt
import numpy as np
from cvxopt.modeling import variable, op
from cvxopt import matrix

filepath = os.path.dirname(__file__) + '/data01.csv'

data = np.genfromtxt(filepath, delimiter=',', dtype=None, encoding='utf-8')

_x, _y = [], []

for label in data:
    _x.append(label[0])
    _y.append(label[1])


def o(ax, bx):
    return np.array([[ax], [bx]])


def p():
    pn = []
    for elem in _x:
        pn.append([elem, 1])
    return np.array(pn)


def pplus():
    return np.linalg.pinv(p())


def xn():
    xn = []
    for elem in _x:
        xn.append([elem, 1])
    return np.array(xn)


def yn():
    yn = []
    for elem in _y:
        yn.append([elem])
    return np.array(yn)


fi = matrix(xn())
theta = variable(2)
tau = variable(len(_x))
y = matrix(yn())

i1 = matrix(1.0, (1, len(_x)))

c1 = (fi * theta - y >= -1 * tau)
c2 = (fi * theta - y <= tau)

p1 = op(i1 * tau, [c1, c2])
p1.solve()

alp = theta[0][0]
blp = theta[1][0]

resultLS = np.matmul(pplus(), yn())

als = resultLS[0][0]
bls = resultLS[1][0]

alp = float(alp.value()[0])
blp = float(blp.value()[0])

print("========")
print("aLP =", alp)
print("bLP =", blp)
print("========")
print("========")
print("aLS =", round(als, 4))
print("bLS =", round(bls, 4))
print("========")

plt.scatter(_x, _y)

x_values = np.linspace(min(_x), max(_x), 100)
y_values = als * x_values + bls
plt.plot(x_values, y_values, color='red', label=f'Prosta: y = {als:.2f}x + {bls:.2f}')

x_values = np.linspace(min(_x), max(_x), 100)
y_values = alp * x_values + blp
plt.plot(x_values, y_values, color='yellow', label=f'Prosta: y = {alp:.2f}x + {blp:.2f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of x and y')

plt.ylim(2, 10)

plt.legend()

plt.show()
