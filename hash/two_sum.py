import sys
sys.path.append("..")
from utils.file_reader import *


def get_data():
    return list(map(lambda s: int(s), read_input(FilePath.TWO_SUM)))


def two_sum():

    def execute(data):
        hash_num = dict()
        for i in range(len(data)):
            hash_num[data[i]] = 1

        num_target_val = 0

        for t in range(-10000, 10001):
            print(t)
            keys = hash_num.keys()
            for x in keys:
                y = t - x
                if y != x and y in keys:
                    num_target_val+=1
                    break

        return num_target_val

    return execute(get_data())


print(two_sum())
# 427
