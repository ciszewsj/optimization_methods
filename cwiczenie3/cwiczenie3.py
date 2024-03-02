import numpy as np
from scipy.io import loadmat
from cvxopt.modeling import variable, op
from cvxopt import matrix, blas, solvers
import matplotlib.pyplot as plt


def create_matrix(n):
    new_matrix = np.zeros((n - 1, n))
    np.fill_diagonal(new_matrix, 1)
    np.fill_diagonal(new_matrix[:, 1:], -1)
    return new_matrix


q = 1

data = loadmat('Data01.mat')

yn = np.array(data['y']).astype(np.double)
tn = np.array(data['t']).astype(np.double)

y = matrix(yn)
t = matrix(tn)

v = variable(len(y))

D = matrix(create_matrix(len(y)))

c1 = (sum(abs(D * v)) <= q)

p1 = op(sum(abs(y - v)), [c1])
p1.solve()

plt.scatter(tn.transpose().tolist()[0], yn.transpose().tolist()[0])

print(v.value)
print(v)
print(np.array(v.value).tolist())

plt.plot(tn.transpose().tolist()[0], np.array(v.value).transpose().tolist()[0], color='red', label=f'Prosta:')

plt.show()
