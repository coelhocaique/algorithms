# Part 1
# In this programming problem and the next you'll code up the greedy algorithms 
# from lecture for minimizing the weighted sum of completion times.
# This file describes a set of jobs with positive and integral weights and lengths. It has the format
# 
# [number_of_jobs]
# 
# [job_1_weight] [job_1_length]
# 
# [job_2_weight] [job_2_length]
# 
# You should NOT assume that edge weights or lengths are distinct.
# 
# Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of 
# the difference (weight - length). 
# Recall from lecture that this algorithm is not always optimal. 
# IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. 
# Beware: if you break ties in a different way, you are likely to get the wrong answer. 
# You should report the sum of weighted completion times of the resulting schedule a positive integer.

# Part 2
# For this problem, use the same data set as in the previous problem. 
# Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). 
# In this algorithm, it does not matter how you break ties. 
# You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

import sys
sys.path.append("..")
from utils.file_reader import *
from queue import PriorityQueue


class JobDiff:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.diff = weight - length

    def __lt__(self, other):
        return self.diff > other.diff or (self.diff == other.diff and self.weight > other.weight)

    def __str__(self):
        return str((self.diff, self.weight, self.length))

class JobRatio:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.diff = weight / length

    def __lt__(self, other):
        return self.diff > other.diff or (self.diff == other.diff and self.weight > other.weight)

    def __str__(self):
        return str((self.diff, self.weight, self.length))

def get_data():
    return list(map(lambda s: map(int, s.strip().split()), read_input(FilePath.JOBS)))


def schedule_jobs(job_type_class):

    def execute(data):
        pq = PriorityQueue()
        weighted_sum = 0
        comp_time = 0
        for weight, length in data:
            pq.put(job_type_class(weight, length))

        while pq.qsize() > 0:
            job = pq.get()
            comp_time+=job.length
            weighted_sum+= (job.weight * comp_time)

        return weighted_sum

    return execute(get_data())


print('Scheduling by diff:', schedule_jobs(JobDiff))
print('Scheduling by ratio:', schedule_jobs(JobRatio))
