import sys
sys.path.append("..")

"""
    This file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

    [number_of_vertices]
    
    [weight of first vertex]
    
    [weight of second vertex]
    
    ...
    
    For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702.
    
    Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set. 
    The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set? 
    (By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.) In the box below, enter a 8-bit string,
     where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. 
     For example, if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other four vertices are not, 
     then you should enter the string 10011010 in the box below.
"""
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
