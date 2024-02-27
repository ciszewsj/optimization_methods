import numpy as np
from cvxopt.modeling import variable, op, sum
import matplotlib.pyplot as plt

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


def res(a, b, xp):
    return a * xp + b


c1 = (alp + blp <= 1)
c2 = (alp + blp >= 1)

# p1 = op(np.array(np.multiply(np.array([[alp], [blp]]), np.array([1, 2])), [c1, c2]))
#
# p1.solve()

# print(np.full(xn(), 1))

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
