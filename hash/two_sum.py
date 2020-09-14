import sys,datetime
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
            keys = hash_num.keys()
            for x in keys:
                y = t - x
                if y != x and hash_num.get(y, None) is not None:
                    num_target_val+=1
                    break

        return num_target_val

    return execute(get_data())


start = datetime.datetime.now()
print("start=", start)
print(two_sum())
print("end=", datetime.datetime.now() - start)
# 427
