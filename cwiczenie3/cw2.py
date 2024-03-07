import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize

data = loadmat('Data01.mat')

x = np.array(data['t']).astype(np.double)
y = np.array(data['y']).astype(np.double)

q = 30


def distance(v):
    return np.linalg.norm(y - v, ord=2)


def l1_constraint(v):
    return q - (np.linalg.norm(v, ord=1))


initial_guess = np.zeros(1001)

constraint = {'type': 'ineq', 'fun': l1_constraint}

max_iterations = 1
options = {'maxiter': max_iterations, "disp": True}

result = minimize(distance, initial_guess, constraints=constraint, options={})

v_optimized = result.x

print("Optimized v:", v_optimized)
print("Norm of x-v:", distance(v_optimized))
print("L1 norm of v:", np.linalg.norm(v_optimized, ord=1))

plt.scatter(x, y)
plt.scatter(x, v_optimized)
plt.show()
