import sys, datetime, time
sys.path.append("..")
from math import inf, sqrt, pow, log2
from utils.file_reader import *

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
