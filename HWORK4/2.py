import numpy as np
import random
def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2
step = 0.005
#積分
def integrate(f, rx, ry, rz):
    area = 0.0
    for x in np.arange(rx[0], rx[1], step):
        for y in np.arange(ry[0], ry[1], step):
            for z in np.arange(rz[0], rz[1], step):
                area += f(x, y, z) * step**3
    return area
#蒙地卡羅
def mcintegrate(f, rx, ry, rz, upper, lower, n=100000):
    hits = 0
    for _ in range(n):
        x = random.uniform(rx[0], rx[1])
        y = random.uniform(ry[0], ry[1])
        z = random.uniform(rz[0], rz[1])
        p = random.uniform(lower, upper)
        if f(x, y, z) > p:
            hits += 1
    return (rx[1] - rx[0]) * (ry[1] - ry[0]) * (rz[1] - rz[0]) * (upper - lower) * (hits / n)
#蒙地卡羅積分法
def mcintegrate_direct(f, rx, ry, rz, n=100000):
    total = 0
    for _ in range(n):
        x = random.uniform(rx[0], rx[1])
        y = random.uniform(ry[0], ry[1])
        z = random.uniform(rz[0], rz[1])
        total += f(x, y, z)
    volume = (rx[1] - rx[0]) * (ry[1] - ry[0]) * (rz[1] - rz[0])
    return total / n * volume
print("黎曼積分法結果:", integrate(f, [0, 1], [0, 1], [0, 1]))
print("蒙地卡羅積分法 (命中法) 結果:", mcintegrate(f, [0, 1], [0, 1], [0, 1], upper=6, lower=0))
print("蒙地卡羅積分法 (直接累加法) 結果:", mcintegrate_direct(f, [0, 1], [0, 1], [0, 1]))