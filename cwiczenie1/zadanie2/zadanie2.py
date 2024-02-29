import numpy as np
import cvxopt as co
from cvxopt.modeling import variable, op, dot, matrix

# 311192 Ciszewksi Jakub
# 311524 Tomczyk Michał

x1 = variable()
x2 = variable()
x3 = variable()

c1 = (2000 <= 70 * x1 + 121 * x2 + 65 * x3)
c12 = (70 * x1 + 121 * x2 + 65 * x3 <= 2250)
c2 = (0 <= 45 * x1 + 40 * x2 + 60 * x3)
c22 = (45 * x1 + 40 * x2 + 60 * x3 <= 1000)
c3 = (5000 <= 107 * x1 + 500 * x2)
c32 = (107 * x1 + 500 * x2 <= 10000)
c4 = (x1 <= 10)
c42 = (0 <= x1)

c5 = (0 <= x2)
c52 = (x2 <= 10)
c6 = (x3 <= 10)
c62 = (0 <= x3)

p1 = op(0.15 * x1 + 0.25 * x2 + 0.05 * x3, [c1, c12, c2, c22, c3, c32, c4, c42, c5, c52, c6, c62])

p1.solve()

x1_value = round(x1.value[0], 4)
x2_value = round(x2.value[0], 4)
x3_value = round(x3.value[0], 4)

print("--------------")
print("x1:", x1_value)
print("x2:", x2_value)
print("x3:", x3_value)
print("--------------")
