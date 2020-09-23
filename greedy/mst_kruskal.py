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

from utils.file_reader import *
from union_find import UnionFind

def get_data():

    lines = list(map(lambda s: s.split(), read_input(FilePath.MST_PRIM)))

    num_nodes, num_edges = map(int, lines[0])

    g = []

    for line in lines[1:]:
        u, v, cost = map(int, line)
        g.append((cost, u, v))

    return g, num_nodes


def kruskal_mst(g, num_nodes):
    total_cost = index = 0
    g.sort()
    uf = UnionFind(num_nodes)

    while uf.size() > 1:
        cost, u, v = g[index]

        if uf.union(u, v):
            total_cost+=cost

        index+=1

    return total_cost


g, num_nodes = get_data()

prims_mst_total_cost = kruskal_mst(g, num_nodes)

print('Kruskal MST total cost:', prims_mst_total_cost)
