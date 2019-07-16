# In this programming problem you'll code up Prim's minimum spanning tree algorithm.
# This file describes an undirected graph with integer edge costs. It has the format
#
# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
#
# You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
#
# Your task is to run Prim's minimum spanning tree algorithm on this graph.
# You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative

import sys
sys.path.append("..")

from trees.heaps import PriorityQueue
from utils.file_reader import *


def get_data():
    g = {}

    def add_edge(u, v):
       pass
    
    lines = map(lambda s: s.split(), read_input(FilePath.MST_PRIM))

    for line in lines[1:]:
        edges = []
        u, v, cost = map(int, line.strip().split())
        vertex = int(line[0])
        if u in g.keys():
            g.get(u).append(v)
        else:
            g[u] = edges




    return g, len(vertices)


def compute_answer(shortest_paths, reported_vertices):
    return ','.join([str(shortest_paths[v]) for v in reported_vertices])


def dijkstra_shortest_path(g, vertices, source, default_distance=1000000):
    distance = [default_distance] * (vertices + 1)
    visited = [False] * (vertices + 1)
    pq = PriorityQueue(mode='min')
    distance[source] = 0

    while vertices > 0:
        edges = g.get(source)
        visited[source] = True

        for edge in edges:
            v, length = edge[0], edge[1]
            length = distance[source] + length
            pq.add((length, v))
        
        pool = True
        while pool and pq.size() > 0:
            length, v = pq.poll()
            if not visited[v]:
                distance[v] = length
                source = v
                pool = False

        vertices -= 1

    return distance


data, num_nodes = get_data()
shortest_paths = dijkstra_shortest_path(data, num_nodes, 1)

print('Dijkstra heap:', compute_answer(shortest_paths, nodes_to_report()))
