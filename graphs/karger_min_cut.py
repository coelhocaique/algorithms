from utils.file_reader import *
import random, sys


def get_data():
    lines = map(lambda s: s.split(), read_input(FilePath.MIN_CUT))
    g = {}

    for line in lines:
        g[int(line[0])] = list(map(lambda s: int(s), line[1:]))

    return g


def karger_min_cut(g):

    def choose_edge_randomly(n_len, g):
        u_rand = random.randint(0, n_len - 1)
        u = list(g.keys())[u_rand]
        v = g.get(u)
        v_index = random.randint(0, len(v) - 1)
        return u, v[v_index]

    def remove_self_loops(u, v, u_edges):
        return [e for e in u_edges if e != u and e != v]

    def contract(u, v, g):
        u_edges = g.pop(u, None)
        v_edges = g.pop(v, None)

        # fuse nodes
        u_edges += v_edges

        # point v edges to u
        for key in g.keys():
            if key != u and key != v:
                edges = g.get(key)
                g[key] = [u if e == v else e for e in edges]

        # remove self loops
        g[u] = remove_self_loops(u, v, u_edges)

        return g

    def get_number_of_edges(g):
        keys = list(g.keys())
        return len(g.get(keys[0]))

    def get_min_cut(g):
        n_len = len(g.keys())
        while n_len > 2:
            u, v = choose_edge_randomly(n_len, g)
            # contract from u to v
            g = contract(u, v, g)
            n_len-=1

        return get_number_of_edges(g)

    return get_min_cut(g)


min_cut = sys.maxsize

for i in range(100):
    g = get_data()
    min_cut_cur = karger_min_cut(g)
    print('iteration %g min_cut=%g' % (i, min_cut_cur))
    min_cut = min(min_cut, min_cut_cur)

print('min_cut: %g' % min_cut)
