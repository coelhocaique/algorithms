import sys
sys.path.append("..")

"""
    In this programming problem you'll code up Prim's minimum spanning tree algorithm.
    This file describes an undirected graph with integer edge costs. It has the format

    [number_of_nodes] [number_of_edges]
    [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
    [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

    You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

    Your task is to run Prim's minimum spanning tree algorithm on this graph.
    You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative
"""

from queue import PriorityQueue
from utils.file_reader import *


def get_data():

    def add_edge(u, v, cost, g):
        g[u].append((cost, v))
    
    lines = list(map(lambda s: s.split(), read_input(FilePath.MST_PRIM)))

    num_nodes, num_edges = map(int, lines[0])
    
    g = [[] for _ in range(num_nodes + 1)]

    for line in lines[1:]:
        u, v, cost = map(int, line)
        add_edge(u, v, cost, g)
        add_edge(v, u, cost, g)

    return g, num_nodes


def prim_mst(g, num_nodes):
    
    def get_start_node():
        return 500    

    def execute(g, num_nodes):
        visited = [False for _ in range(num_nodes + 1)]
        cur_node = get_start_node()
        total_cost = 0
        pq = PriorityQueue()

        while num_nodes > 0:    
            visited[cur_node] = True

            for cost, v in g[cur_node]:
                pq.put((cost, v))

            while pq.qsize() > 0:
                cost, v = pq.get()
                if not visited[v]:
                    cur_node = v
                    total_cost+=cost
                    break

            num_nodes-=1

        return total_cost

    return execute(g, num_nodes)    

g, num_nodes = get_data()
prims_mst_total_cost = prim_mst(g, num_nodes)

print('Prim MST total cost:', prims_mst_total_cost)
