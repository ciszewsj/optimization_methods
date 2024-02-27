import matplotlib.pyplot as plt
import numpy as np
from cvxopt.modeling import variable, op

data = np.genfromtxt('data01.csv', delimiter=',', dtype=None, encoding='utf-8')

_x, _y = [], []

for label in data:
    _x.append(label[0])
    _y.append(label[1])


def o(ax, bx):
    return np.array([[ax], [bx]])


def p():
    pn = []
    for elem in _x:
        pn.append([elem, 1])
    return np.array(pn)


def pplus():
    return np.linalg.pinv(p())


def yn():
    yn = []
    for elem in _y:
        yn.append([elem])
    return np.array(yn)


def xn():
    xn = []
    for elem in _x:
        xn.append([elem])
    return np.array(xn)


alp = variable()
blp = variable()

va = variable()
vb = variable()


def res(ax, bx, xp):
    return ax * xp + bx


c1 = (alp + blp <= 1)
c2 = (alp + blp >= 1)


# Assuming `op` is an optimization function from some library
def solve_problem(a, b):
    res = 0
    for i in range(0, len(_x)):
        res += abs(a * float(_x[i]) + b - float(_y[i]))
    return res


p1 = op(solve_problem(alp, blp), [])
p1.solve()

resultLS = np.matmul(pplus(), yn())

als = resultLS[0][0]
bls = resultLS[1][0]

print("========")
print("aLP =", alp.value)
print("bLP =", blp.value)
print("========")
print("========")
print("aLS =", round(als, 4))
print("bLS =", round(bls, 4))
print("========")

plt.scatter(_x, _y)

alp = float(alp.value[0])
blp = float(blp.value[0])

x_values = np.linspace(min(_x), max(_x), 100)
y_values = als * x_values + bls
plt.plot(x_values, y_values, color='red', label=f'Prosta: y = {als:.2f}x + {bls:.2f}')

x_values = np.linspace(min(_x), max(_x), 100)
y_values = alp * x_values + blp
plt.plot(x_values, y_values, color='green', label=f'Prosta: y = {alp:.2f}x + {blp:.2f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of x and y')

plt.legend()

plt.show()
