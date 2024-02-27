import numpy as np
from cvxopt.modeling import variable, op

data = np.genfromtxt('data01.csv', delimiter=',', dtype=None, encoding='utf-8')

_x, _y = [], []
new_dict = {}
for label in data:
    _x.append(label[0])
    _y.append(label[1])
    new_dict[label[0]] = label[1]



