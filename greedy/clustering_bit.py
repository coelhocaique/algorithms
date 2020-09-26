import sys
sys.path.append("..")

from utils.file_reader import *
from union_find import UnionFind


def get_data():

    lines = list(map(lambda s: s.split(), read_input(FilePath.CLUSTERING_BITS)))
    num_nodes = int(lines[0][0])
    g = dict()

    for i in range(1, len(lines)):
        node = ''.join(lines[i])
        g[node] = i

    return g, num_nodes


def get_one_bit_candidates(node, g):
    candidates = []
    for i in range(len(node)):
        change_to = '1' if node[i] == '0' else '0'
        candidate = node[:i] + change_to + node[i+1:]
        candidate_index = g.get(candidate, None)

        if candidate_index is not None:
            candidates.append(candidate_index)

    return candidates


def get_two_bit_candidates(node, g):
    candidates = []
    for i in range(len(node)):
        i_change_to = '1' if node[i] == '0' else '0'
        i_changed = node[:i] + i_change_to + node[i+1:]
        for j in range(len(node)):
            j_change_to = '1' if node[i] == '0' else '0'
            candidate = i_changed[:j] + j_change_to + i_changed[j+1:]
            candidate_index = g.get(candidate, None)

            if candidate_index is not None:
                candidates.append(candidate_index)

    return candidates


def clustering(g, num_nodes):
    uf = UnionFind(num_nodes)

    for node in g.keys():
        u = g.get(node)
        one_bit_candidates = get_one_bit_candidates(node, g)
        two_bit_candidates = get_two_bit_candidates(node, g)

        for v in one_bit_candidates:
            uf.union(u, v)

        for v in two_bit_candidates:
            uf.union(u, v)

    return len(set(uf.leaders())) - 1


g, num_nodes = get_data()

max_distance = clustering(g, num_nodes)

print('Clustering bit max distance:', max_distance)  # 6118

