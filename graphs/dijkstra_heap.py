import sys
sys.path.append("..")

from trees.heaps import PriorityQueue
from utils.file_reader import *


def nodes_to_report():
    return [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]


def get_data():
    g = {}
    vertices = set()
    lines = map(lambda s: s.split(), read_input(FilePath.DIJKSTRA))

    for line in lines:
        edges = []
        for i in range(1, len(line)):
            u, length = map(int, line[i].strip().split(','))
            edges.append((u, length))
            vertices.add(u)

        vertex = int(line[0])
        g[vertex] = edges
        vertices.add(vertex)

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
