import numpy as np
import cvxopt as co
from cvxopt.modeling import variable, op, dot, matrix

# 311192 Ciszewksi Jakub
# 311524 Tomczyk Michał

lek1 = variable()
lek2 = variable()
sur1 = variable()
sur2 = variable()


def fcosts(xsur1, xsur2, xlek1, xlek2):
    return 100 * xsur1 + 199.9 * xsur2 + 700 * xlek1 + 800 * xlek2


def fincom(xlek1, xlek2):
    return 6500 * xlek1 + 7100 * xlek2


c1 = (0.01 * sur1 + 0.02 * sur2 + -0.5 * lek1 - 0.6 * lek2 >= 0)
c2 = (sur1 + sur2 <= 1000)
c3 = (90 * lek1 + 100 * lek2 <= 2000)
c4 = (40 * lek1 + 50 * lek2 <= 800)
c5 = (100 * sur1 + 199.9 * sur2 + 700 * lek1 + 800 * lek2 <= 100000)
c6 = (lek1 >= 0)
c7 = (lek2 >= 0)
c8 = (sur1 >= 0)
c9 = (sur2 >= 0)

p1 = op(fcosts(sur1, sur2, lek1, lek2) - fincom(lek1, lek2), [c1, c2, c3, c4, c5, c6, c7, c8, c9])
p1.solve()

x1_value = round(sur1.value[0], 4)
x2_value = round(sur2.value[0], 4)
x3_value = round(lek1.value[0], 4)
x4_value = round(lek2.value[0], 4)

print("--------------")
print("lek1:", x3_value)
print("lek2:", x4_value)
print("sur1:", x1_value)
print("sur2:", x2_value)
print("--------------")
