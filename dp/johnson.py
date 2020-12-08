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
from bellman_ford import BellmanFord
from queue import PriorityQueue


def get_data(file_path):
    lines = list(map(lambda s: s.split(), read_input(file_path)))
    num_nodes = int(lines[0][0])
    incoming_g = dict()
    outcoming_g = dict()

    for line in lines[1:]:
        u, v, cost = map(int, line)
        u, v = u+1, v+1 # add one to u and v to add zero node as 1 later

        outcoming_g[u] = outcoming_g.get(u, []) + [(v, cost)]
        incoming_g[v] = incoming_g.get(v, []) + [(u, cost)]


    return incoming_g, outcoming_g, num_nodes


def dijkstra_shortest_path(g, vertices, source, default_distance=1000000):
    distance = [default_distance] * (vertices + 1)
    visited = [False] * (vertices + 1)
    pq = PriorityQueue()
    distance[source] = 0

    while vertices > 0:
        edges = g.get(source, [])
        visited[source] = True

        for edge in edges:
            v, length = edge[0], edge[1]
            length = distance[source] + length
            pq.put((length, v))

        pool = True
        while pool and pq.qsize() > 0:
            length, v = pq.get()
            if not visited[v]:
                distance[v] = length
                source = v
                pool = False

        vertices -= 1

    return distance

def johnson(incoming_edges_g, outcoming_edges_g, n):

    # add_new_vertex from 0 to every graph vertex
    for k in range(2, n+2):
        incoming_edges_g[k] = incoming_edges_g.get(k, []) + [(1, 0)]

    # run_bellman_ford and check if there is negative cycle
    bf = BellmanFord(graph=incoming_edges_g, vertices=n+1, source=1)

    bf.compute_shortest_path()

    if bf.has_negative_cost_cycle:
        return None

    reweighted_graph = {}

    # reweight edges
    for u in outcoming_edges_g.keys():
        src_sp = bf.shortest_path(u)
        reweighted_edges = []

        for v, cost in outcoming_edges_g[u]:
            dst_sp = bf.shortest_path(v)
            cost_reweighted = cost + src_sp - dst_sp
            reweighted_edges.append((v, cost_reweighted))

        reweighted_graph[u] = reweighted_edges

    # run djikstra
    shortest_shortest_paths = [[], []]
    for i in range(2, n+2):
        shortest_paths = dijkstra_shortest_path(reweighted_graph, n+1, i, inf)
        shortest_shortest_paths.append(shortest_paths)

    # extract_original_edge_length
    shortest_path = (0, 0, inf)
    for u in range(2, n+2):
        for v in range(u+1, n+2):
            sp = shortest_shortest_paths[u][v]
            pu = bf.shortest_path(u)
            pv = bf.shortest_path(v)
            original_edge_length = sp - pu + pv
            shortest_shortest_paths[u][v] = original_edge_length

            if original_edge_length < shortest_path[2]:
                shortest_path = (u-1, v-1, original_edge_length)

    return shortest_path

def shortest_shortest_path():
    data = [get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_1), get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_2), get_data(FilePath.ALL_PAIRS_SHORTEST_PATH_3)]
    has_result = False
    shortest_path = None
    index = 1
    for g in data:
        start = time.time()
        print('dataset %d start time %s' % (index, datetime.datetime.now()))
        result = johnson(g[0], g[1], g[2])
        print('dataset %d processed in %s seconds' % (index, (time.time() - start)))
        print('result =', result)
        if result is not None:
            has_result = True
            if shortest_path is None or shortest_path[2] > result[2]:
                shortest_path = result
        index+=1

    if has_result:
        print(shortest_path)
        return shortest_path[2]
    else:
        return 'NULL'


print('Johnson Shortest shortest path: ', shortest_shortest_path())