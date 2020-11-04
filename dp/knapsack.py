import sys, time
sys.path.append("..")

"""
   This file describes a knapsack instance, and it has the following format:

    [knapsack_size][number_of_items]
    
    [value_1] [weight_1]
    
    [value_2] [weight_2]
    
    ...
    
    For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.
    
    This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.
    
    In the box below, type in the value of the optimal solution.
    
    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum! 
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