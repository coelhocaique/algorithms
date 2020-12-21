import sys, datetime, time
sys.path.append("..")
from math import inf, sqrt, pow, log2
from utils.file_reader import *

"""
    In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures.  
    Here is a data file describing a TSP instance.

    The first line indicates the number of cities.  Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.  

    The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} 
    (x−z) 2 +(y−w) 2 between them.  

    In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

    OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here.  
    The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that.  
    What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

    HINT: You might experiment with ways to reduce the data set size.  For example, trying plotting the points.  
    Can you infer any structure of the optimal solution?  Can you use that structure to speed up your algorithm?

"""

class City:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def get_data():
    lines = list(map(lambda s: s.split(), read_input(FilePath.TSP)))
    num_nodes = int(lines[0][0])
    cities = []

    for line in lines[1:]:
        cities.append(City(float(line[0]), float(line[1])))

    return cities, num_nodes

def euclidean_distance(a, b):
    return sqrt(pow(a.latitude - b.latitude, 2) + pow(a.longitude - b.longitude, 2))

def generate_bit_mask_cache(n):
    cache = {}

    for bitmask in range(1, (1 << n) - 1):
        cache[bitmask | 1] = {1: inf if bitmask != 1 else 0}

    return cache

def generate_bitmask(m):
    for bitmask in range(1,(1<<m)-1):
        yield bitmask | 1

def get_destination_edges(bitmask,excluded_node=None):
    while bitmask:
        b = bitmask & (~bitmask+1)
        if b != excluded_node or excluded_node is None:
            yield int(log2(b) + 1)
        bitmask ^= b

def exclude_node_from_mask(bitmask,node):
    return bitmask & ~(1 << (node - 1))

def get_last_node_with_all_possibilities(n):
    return (1<<n)-1

def tsp(cities, n):
    cache = {1: {1:0}}

    for m in range(2, n+1):
        print("m=%d" % m)

        for subset_s in generate_bitmask(m):
            for j in get_destination_edges(subset_s, excluded_node=1):
                subset_s_minus_j = exclude_node_from_mask(subset_s, j)
                min_iteration_cost = inf

                for k in get_destination_edges(subset_s_minus_j):
                    previous_result = cache.get(subset_s_minus_j, None)
                    if previous_result is not None:
                        ckj = euclidean_distance(cities[k-1], cities[j-1])

                        iteration_result = previous_result.get(k, inf) + ckj

                        min_iteration_cost = min(min_iteration_cost, iteration_result)

                if cache.get(subset_s, None) is not None:
                    cache[subset_s][j] = min_iteration_cost
                else:
                    cache[subset_s] = {j: min_iteration_cost}

    all_cities_result = cache[get_last_node_with_all_possibilities(n)]
    min_cost = inf
    for j in all_cities_result:
        if j != 1:
            current_cost = all_cities_result[j] + euclidean_distance(cities[0], cities[j-1])
            min_cost = min(min_cost, current_cost)

    return min_cost

start = time.time()

print('TSP start time: %s' % datetime.datetime.now())
cities, n = get_data()
min_distance = tsp(cities, n)
print('TSP min distance = %d' % min_distance)

print('TSP finish time: %s' % datetime.datetime.now())
print('Total time elapsed: %f' % (time.time() - start))

#26442 - 3988.148043 seconds pypy
