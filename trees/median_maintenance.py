import sys
sys.path.append("..")
from utils.file_reader import *
from trees.heaps import PriorityQueue


def get_data():
    return list(map(lambda s: int(s), read_input(FilePath.MEDIAN_MAINTENANCE)))


def compute_answer(medians):
    return sum(medians) % 10000


def median():

    def balance_trees(pqmax, pqmin, n):
        pqmax.add(n)
        diff = pqmax.size() - pqmin.size()
        while diff > 1:
            pqmin.add(pqmax.poll())
            diff-=1

        if pqmin.size() > 0 and pqmin.peek() > pqmax.peek():
            pmax = pqmax.poll()
            pmin = pqmin.poll()
            pqmax.add(pmin)
            pqmin.add(pmax)

    def execute(data):
        pqmin = PriorityQueue(mode='max')
        pqmax = PriorityQueue(mode='min')
        medians = []
        for i in range(len(data)):
            num = data[i]
            balance_trees(pqmax, pqmin, num)
            medians.append(pqmin.peek() if (i + 1) % 2 == 0 else pqmax.peek())

        return medians

    return execute(get_data())


medians = median()
print(medians)
print(compute_answer(medians))
