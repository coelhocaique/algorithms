import sys
sys.path.append("..")
from utils.file_reader import *


def get_data():
    return list(map(lambda s: int(s), read_input(FilePath.MWIS)))[1:]


def compute_mwis(weights):
    weights_to_report = [1, 2, 3, 4, 17, 117, 517, 997]
    output = ['0'] * len(weights_to_report)

    for i in range(len(weights_to_report)):
        w = weights_to_report[i]
        if w <= len(weights):
            output[i] = str(weights[w-1])

    return ''.join(output)


def execute(weights):
    cache = [0] * (len(weights) + 1)
    weights_used = [0] * len(weights)

    cache[0], cache[1] = 0, weights[0]

    for i in range(2, len(weights)+1):
        cache[i] = max(cache[i-1], cache[i-2] + weights[i-1])

    i = len(weights)

    while i >= 1:
        if cache[i-1] >= cache[i-2] + weights[i-1]:
            i-=1
        else:
            weights_used[i-1] = 1
            i-=2

    return weights_used


weights = execute(get_data())
print(compute_mwis(weights))
