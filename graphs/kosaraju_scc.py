# Strongly connected components Kosaraju's algorithm
from utils.file_reader import *
import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def get_data():
    lines = map(lambda s: s.split(), read_input(FilePath.SCC))
    g, g_inverted = {}, {}
    nodes = set()

    for line in lines:
        src = int(line[0])
        dst = int(line[1])

        if src in g.keys():
            g.get(src).append(dst)
        else:
            g[src] = [dst]

        if dst in g_inverted.keys():
            g_inverted.get(dst).append(src)
        else:
            g_inverted[dst] = [src]

        nodes.add(src)
        nodes.add(dst)

    return g, g_inverted, len(nodes)


def compute_answer(leaders):
    aux = []
    for k in leaders.keys():
        aux.append(len(leaders.get(k)))

    aux.sort(reverse=True)
    out = [0] * 5
    for i in range(len(out)):
        if i < len(aux):
            out[i] = str(aux[i])

    return ','.join(out)


def kosaraju():

    def dfs(g, node, visited, res=[]):
        visited[node] = True
        neighbours = g.get(node)
        if neighbours:
            for cur_node in neighbours:
                if not visited[cur_node]:
                    dfs(g, cur_node, visited, res)

        res.append(node)

        return res

    def change_vertices(g, finishing_times):
        new_g = {}
        ft_length = len(finishing_times)
        oft = [0] * ft_length

        for i in range(ft_length):
            oft[finishing_times[i] - 1] = i + 1

        for i in range(ft_length):
            u = finishing_times[i]
            neighbours = g.get(u)
            new_neighbours = []
            if neighbours:
                for n in neighbours:
                    new_neighbours.append(oft[n - 1])

            new_g[oft[u - 1]] = new_neighbours

        return new_g

    def compute_finishing_times(g_inverted, vertices, visited):
        finishing_times = []
        for node in reversed(range(1, vertices + 1)):
            if not visited[node]:
                dfs(g_inverted, node, visited, finishing_times)

        return finishing_times

    def compute_scc(g, finishing_times, vertices, visited):
        new_g = change_vertices(g, finishing_times)
        result = {}
        for node in reversed(range(1, vertices + 1)):
            if not visited[node]:
                result[node] = dfs(new_g, node, visited, [])

        return result

    def scc():
        g, g_inverted, vertices = get_data()
        visited = [False] * (vertices + 1)
        finishing_times = compute_finishing_times(g_inverted, vertices, list(visited))
        leaders_dict = compute_scc(g, finishing_times, vertices, list(visited))
        return compute_answer(leaders_dict)

    return scc()


def main():
    print(kosaraju())


thread = threading.Thread(target=main)
thread.start()
