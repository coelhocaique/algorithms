import sys
sys.path.append("..")
from math import inf


""" 
    Bellman-Ford algorithm to compute shortest path between a node and all other nodes
    Input: 
        graph: a dict with key (src, dest) and value an array of costs
        vertices: total amount of vertices
        source: the source index to compute shortest paths
"""

class BellmanFord:

    def __init__(self, graph, vertices, source):
        self.vertices = vertices
        self.graph = graph
        self.s = source
        self.cache = [[inf for _ in range(vertices+1)]]
        self.has_negative_cost_cycle = False


    def __optimize_space__(self, iteration_cache_results):
        if len(self.cache) == 1:
            self.cache.append(iteration_cache_results)
        else:
            self.cache[0] = self.cache[1]
            self.cache[1] = iteration_cache_results

    def __check_negative_cost_cycle__(self):
        self.has_negative_cost_cycle = self.cache[-2] != self.cache[-1]
        return self.has_negative_cost_cycle

    def compute_shortest_path(self):
        self.cache[0][self.s] = 0

        for i in range(1, self.vertices+1):
            iteration_cache_results = [self.cache[-1][0]]

            for v in range(1, self.vertices+1):
                min_edge = inf
                incoming_edges = self.graph.get(v, [])

                if len(incoming_edges) > 0:
                    min_edge = min(self.cache[-1][w[0]] + w[1] for w in incoming_edges)

                current_min_cost = min(self.cache[-1][v], min_edge)

                iteration_cache_results.append(current_min_cost)

            self.__optimize_space__(iteration_cache_results)

        return self.__check_negative_cost_cycle__()

    def shortest_path(self, v):
        return self.cache[-2][v] if v <= self.vertices else None

