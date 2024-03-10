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

D = matrix(create_matrix(len(y)))

n = len(y)
m = len(y)

v = variable(len(y))
E = variable(len(y))
Q = variable(len(y))

A = np.array([
    [np.eye(n), -1 * np.eye(n), np.zeros((n, m))],
    [-1 * np.eye(n), -1 * np.eye(n), np.zeros((n, m))],
    [np.zeros((1, n)), np.zeros((1, n)), np.ones(m).transpose()],
    [-1 * D, np.zeros((m, n)), -1 * np.eye(m)],
    [D, np.zeros((m, n)), -1 * np.eye(m)]
])

c = matrix(np.array([np.zeros(n), np.ones(n), np.ones(m)])).T

b = matrix(np.array([y, -1 * y, q, np.zeros(m), np.zeros(m)])).T

x = np.array([v, E, Q]).transpose()

c1 = (A * x <= b)
p1 = op(sum(abs(matrix(np.ones(n)).T * E)), [c1])
p1.solve()
