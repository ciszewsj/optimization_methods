import numpy as np
from cvxopt.modeling import variable, op

data = np.genfromtxt('data01.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

data_dict = {name: data[name] for name in data.dtype.names}

alp = variable()
blp = variable()

als = variable()
bls = variable()


def flp(ax, bx, datas):
    res = 0
    for i in range(0, len(datas["x"])):
        res += abs(ax * float(datas["x"][i]) + bx - float(datas["y"][i]))
    return res


def fls(ax, bx, datas):
    res = 0
    for i in range(0, len(datas["x"])):
        res += (ax * float(datas["x"][i]) + bx - float(datas["y"][i])) ** 2
    return res


c1 = (alp >= 0)
c2 = (blp >= 0)

p1 = op(flp(alp, blp, data_dict), [])
p2 = op(flp(als, bls, data_dict), [])
p1.solve()
p2.solve()

print("========")
print("a =", alp.value)
print("b =", blp.value)
print("========")
print("========")
print("a =", als.value)
print("b =", bls.value)
print("========")
