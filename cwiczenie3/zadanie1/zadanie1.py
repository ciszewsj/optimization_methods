import os

import matplotlib.pyplot as plt
import numpy as np
from cvxopt import matrix
from cvxopt.modeling import variable, op
from scipy.io import loadmat


def create_matrix(n):
    new_matrix = np.zeros((n - 1, n))
    np.fill_diagonal(new_matrix, 1)
    np.fill_diagonal(new_matrix[:, 1:], -1)
    return new_matrix


q = 2
r = 10

data = loadmat(os.path.dirname(__file__) + '/../Data01.mat')

yn = np.array(data['y']).astype(np.double)
tn = np.array(data['t']).astype(np.double)

y = matrix(yn)
t = matrix(tn)

v = variable(len(y))
v2 = variable(len(y))

D = matrix(create_matrix(len(y)))

c1 = (sum(abs(D * v)) <= q)
p1 = op(sum(abs(y - v)), [c1])
p1.solve()

p2 = op(sum(abs(y - v2)) + r * sum(abs(D * v2)), [])
p2.solve()

plt.scatter(tn.transpose().tolist()[0], yn.transpose().tolist()[0])

plt.plot(tn.transpose().tolist()[0], np.array(v.value).transpose().tolist()[0], color='red', label=f'q param')

plt.plot(tn.transpose().tolist()[0], np.array(v2.value).transpose().tolist()[0], color='purple', label=f'r param')

plt.show()
