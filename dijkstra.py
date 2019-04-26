# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex)
# as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph.
# a vertex vv and vertex 1, we'll define the shortest-path distance between 1 and vv to be 1000000.
# If there is no path between you should report the shortest-path distances to the following ten vertices,
# in order: 7,37,59,82,99,115,133,165,188,197.
# You should encode the distances as a comma-separated string of integers.
# So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex
# 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000.
# Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above
# ten vertices are given. The string should not contain any spaces.

from file_reader import *
from queue import PriorityQueue


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
    pq = PriorityQueue()
    distance[source] = 0

    while vertices > 0:
        edges = g.get(source)
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


data, num_nodes = get_data()
shortest_paths = dijkstra_shortest_path(data, num_nodes, 1)

print(compute_answer(shortest_paths, [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]))
