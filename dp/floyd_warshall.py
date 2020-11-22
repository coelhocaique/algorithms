import sys, time, datetime
from math import inf
sys.path.append("..")

"""
    The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

    Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute \min_{u,v \in V} d(u,v)min 
    u,v∈V d(u,v), where d(u,v)d(u,v) denotes the shortest-path distance from uu to vv).

    If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, 
    then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, 
    then enter the smallest of the lengths of their shortest shortest paths in the box below.
"""
from utils.file_reader import *


def get_data(file_path):
    lines = list(map(lambda s: s.split(), read_input(file_path)))
    num_nodes = int(lines[0][0])
    g = dict()

    for line in lines[1:]:
        u, v, cost = map(int, line)
        key = (u, v)
        g[key] = min(cost, g.get(key, inf))

    return g, num_nodes

def floyd_warshall(g, n):

    def initialize_cache():
        cache = []

        for i in range(n+1):
            cache.append([])
            for j in range(n+1):
                cost = g.get((i, j), None)

                if i == j:
                    cache[i].append(0)
                elif cost is not None:
                    cache[i].append(cost)
                else:
                    cache[i].append(inf)

        return cache

    def execute_calculation(cache):
        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    cache[i][j] = min(cache[i][j], cache[i][k] + cache[k][j])


    def has_negative_cost_cycle(cache):
        for i in range(n+1):
            if cache[i][i] < 0:
                return True

        return False

    def get_shortest_path(cache):
        if not has_negative_cost_cycle(cache):
            shortest_path = (0, 0, inf)
            for i in range(1, n+1):
                for j in range(1, n+1):
                    cur_val = cache[i][j]
                    if cur_val != 0 and cur_val < shortest_path[2]:
                        shortest_path = (i, j, cur_val)

            return shortest_path

        return None

    cache = initialize_cache()
    execute_calculation(cache)

    return get_shortest_path(cache)


def shortest_shortest_path():
    data = [get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_1), get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_2), get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_3)]
    has_result = False
    shortest_path = None
    index = 1
    for g in data:
        start = time.time()
        print('dataset %d start time %s' % (index, datetime.datetime.now()))
        result = floyd_warshall(g[0], g[1])
        print('dataset %d processed in %s seconds' % (index, (time.time() - start)))
        print('result =', result)

        if result is not None:
            has_result = True
            if shortest_path is None or shortest_path[2] > result[2]:
                shortest_path = result


    if has_result:
        print(shortest_path)
        return shortest_path[2]
    else:
        return 'NULL'


print('Floyd-Warshall shortest shortest path: ', shortest_shortest_path())

#-19