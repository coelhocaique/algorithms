# Strongly connected components Kosaraju's algorithm
import file_reader as fr
import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


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
                new_neighbours.append(oft[n-1])

        new_g[oft[u-1]] = new_neighbours

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


def scc():
    g, g_inverted, vertices = fr.read_scc_input(fr.FilePath.SCC)
    visited = [False] * (vertices + 1)
    finishing_times = compute_finishing_times(g_inverted, vertices, list(visited))
    leaders_dict = compute_scc(g, finishing_times, vertices, list(visited))
    return compute_answer(leaders_dict)


def main():
    print(scc())


thread = threading.Thread(target=main)
thread.start()
