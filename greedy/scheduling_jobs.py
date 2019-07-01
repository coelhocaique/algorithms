import sys
sys.path.append("..")
from utils.file_reader import *
from queue import PriorityQueue


class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.diff = weight - length

    def __lt__(self, other):
        return self.diff < other.diff or (self.diff == other.diff and self.weight > other.weight)

    def __str__(self):
        return str((self.diff, self.weight, self.length))


def get_data():
    return list(map(lambda s: map(int, s.strip().split()), read_input(FilePath.JOBS)))


def schedule_jobs():

    def execute(data):
        pq = PriorityQueue()
        weighted_sum = 0
        comp_time = 0
        for weight, length in data:
            pq.put(Job(weight, length))

        while pq.qsize() > 0:
            job = pq.get()
            comp_time+=job.length
            weighted_sum+= (job.weight * comp_time)

        return weighted_sum

    return execute(get_data())


print(schedule_jobs())
# diff=188635738448
# ratio=190444405675
