import numpy as np
import cvxopt as co
from cvxopt.modeling import variable, op, dot, matrix

data = np.genfromtxt('data01.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

data_dict = {name: data[name] for name in data.dtype.names}


def resultArr(a, b):
    return np.array([[a], [b]])

def senodArr(xArr):
    np.array()


print(data_dict)
