from cvxopt import normal
from cvxopt.modeling import variable, op, constraint
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data01.csv', delimiter=',', dtype=None, encoding='utf-8')

_x, _y = [], []

for label in data:
    _x.append(label[0])
    _y.append(label[1])

a = variable(2)
b = variable()

tau = variable(len(_x))
constraints = []
A = normal(10, 10)
print(type(A), type(a))


def sum_list(variables):
    return sum(variables)


p1 = op(sum_list(tau), constraints)
p1.solve()
