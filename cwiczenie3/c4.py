import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize

data = loadmat('Data01.mat')

t = np.array(data['t']).astype(np.double)

y = np.array(data['y']).astype(np.double).flatten()
D = np.diag(np.ones(len(y))) - np.diag(np.ones(len(y) - 1), 1)
D = D[:-1, :]
q = 2


# Define the objective function to minimize
def objective(v, y_bar, D):
    return np.linalg.norm(y_bar - v, ord=2)


# Define the constraint function
def constraint(v, D, q):
    return np.linalg.norm(D @ v, ord=1) - q


# Initial guess for v
v0 = np.zeros(D.shape[1])  # Assuming D is a matrix with appropriate dimensions

# Define the bounds for v (optional)
bounds = [(None, None)] * len(v0)  # No specific bounds for v

# Define the equality constraint (optional)
eq_constraint = {'type': 'eq', 'fun': constraint, 'args': (D, q)}

# Minimize the objective function subject to the constraint
result = minimize(objective, v0, args=(y, D), constraints=eq_constraint, bounds=bounds)

# Extract the optimized v
optimized_v = result.x

# Print the optimized v
print(f"Optimized v: {optimized_v}")
plt.scatter(t.tolist(), y.tolist(), c='r')

plt.plot(t.tolist(), optimized_v, c='b')

plt.show()
