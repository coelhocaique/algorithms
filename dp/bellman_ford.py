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
        self.cache = [[inf for _ in range(vertices+1)] for _ in range(vertices)]
        self.sp = dict()

    def compute_shortest_path(self):
        self.cache[0][self.s] = 0

        for i in range(1, self.vertices-1):
            for v in range(1, self.vertices+1):
                costs = self.graph.get((i, v), None)
                if costs is not None:
                    self.cache[i][v] = min(self.cache[i-1][v], self.cache[i-1][i] + min(costs))
                else:
                    self.cache[i][v] = self.cache[i-1][v]


        for v in range(1, self.vertices+1):
            self.sp[(self.s, v)] = self.cache[self.vertices-2][v]

        return self.sp


    def shortest_path(self, v):
        return self.cache[self.vertices-2][v] if v <= self.vertices else None


"""
    graph = {
        (1, 2): [5],
        (1, 3): [4],
        (2, 3): [2],
        (2, 4): [3],
        (3, 1): [1],
        (3, 2): [1]
    }
    
    bf = BellmanFord(graph=graph, vertices=4, source=1)
    
    print(bf.compute_shortest_path())

"""
