import sys
sys.path.append("..")
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


def dijkstra_shortest_path(g, vertices, default_distance=1000000):
    dist = [default_distance] * (vertices + 1)
    dist[1] = 0
    visited = [False] * (vertices + 1)

    def get_min_dist_vertex():
        min_dist = sys.maxsize

        for v in range(1, vertices + 1):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def compute(vertices):
        while vertices > 0:
            u = get_min_dist_vertex()
            visited[u] = True
            neighbours = g.get(u)
            for n, l in neighbours:
                dist[n] = min(dist[u] + l, dist[n])
            vertices-=1

        return dist

    return compute(vertices)


data, num_nodes = get_data()
shortest_paths = dijkstra_shortest_path(data, num_nodes)

print('Dijkstra:', compute_answer(shortest_paths, nodes_to_report()))
