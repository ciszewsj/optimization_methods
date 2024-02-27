from cvxopt.modeling import variable, op
from cvxopt import matrix
import numpy as np

data = np.genfromtxt('data01.csv', delimiter=',', dtype=None, encoding='utf-8')

_x, _y = [], []
r = []

for label in data:
    _x.append(label[0])
    _y.append(label[1])

a = variable()
b = variable()

c1 = (a * _x + b - r <= _y)
c2 = (-1* a * _x + b - r <= _y)

p1 = op(sum(r), [c1, c2, c3, c4, c5, c6, c7, c8, c9])
p1.solve()
