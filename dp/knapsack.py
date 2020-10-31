import sys, time
sys.path.append("..")

"""
    
"""
from utils.file_reader import *


def get_data():
    data = list(map(lambda s: (int(s.split()[0]), int(s.split()[1])), read_input(FilePath.KNAPSACK2)))
    return data[0][0], data[1:]


def knapsack(k, vw):
    n = len(vw)
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for x in range(k+1):
            v, w = vw[i-1]
            if x-w >= 0:
                cache[i][x] = max(cache[i-1][x], cache[i-1][x-w] + v)
            else:
                cache[i][x] = cache[i-1][x]

    return cache[n][k]


start = time.time()

k, vw = get_data()
max_capacity = knapsack(k, vw)
print('Knapsack max capacity:', max_capacity)
print((time.time() - start), 'seconds')

# 1=2493893 0.6840760707855225 seconds
# 2=4243395 324.13955521583557 seconds (pypy)