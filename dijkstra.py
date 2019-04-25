import file_reader as fr
from queue import PriorityQueue


def get_data():
    g = {}
    vertices = set()
    lines = fr.read_dijkstra_input(fr.FilePath.DIJKSTRA)

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


def shortest_path(g, vertices, source):
    dist = [1000000] * (vertices + 1)
    visited = [False] * (vertices + 1)

    pq = PriorityQueue()

    dist[source] = 0

    while vertices > 0:
        edges = g.get(source)
        visited[source] = True

        for edge in edges:
            v, length = edge[0], edge[1]
            length = dist[source] + length
            pq.put((length, v))

        pool = True
        while pool and pq.qsize() > 0:
            length, v = pq.get()
            if not visited[v]:
                dist[v] = length
                source = v
                pool = False

        vertices-=1

    return dist


def dijkstra(reported_vertices):
    g, vertices = get_data()
    paths = shortest_path(g, vertices, 1)
    out = []

    for r in reported_vertices:
        out.append(str(paths[r]))

    return dist, out


to_report = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

dist, result = dijkstra(to_report)

print(','.join(result))