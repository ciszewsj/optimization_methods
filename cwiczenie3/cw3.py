import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize

# Zdefiniuj wektor x (przykładowy)


data = loadmat('Data01.mat')

t = np.array(data['t']).astype(np.double)

x = np.array(data['y']).astype(np.double).flatten()
D = np.diag(np.ones(len(x))) - np.diag(np.ones(len(x) - 1), 1)
D = D[:-1, :]


# Definiuj funkcję obliczającą normę euklidesową ||v - x||
def euclidean_norm(v):
    return np.linalg.norm(x - v, 1)


def sum_constraint(v):
    return 2 - np.linalg.norm(np.dot(D, v), 1)


# Początkowe przybliżenie dla wektora v
initial_guess = np.zeros_like(x)  # Początkowe przybliżenie: wektor zerowy tej samej długości co x

constraints = {'type': 'ineq', 'fun': sum_constraint}

# Zminimalizuj normę euklidesową ||v - x||
result = minimize(euclidean_norm, initial_guess, constraints=constraints)

# Wyświetl wynik
v_optimized = result.x
print("Zoptymalizowany v:", v_optimized)
print("Norma euklidesowa ||v - x||:", euclidean_norm(v_optimized))
print("Norma euklidesowa ||v - x||:", sum_constraint(v_optimized))

plt.scatter(t.tolist(), x.tolist(), c='r')

plt.plot(t.tolist(), v_optimized, c='b')

plt.show()
