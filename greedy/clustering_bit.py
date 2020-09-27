import sys
sys.path.append("..")

from utils.file_reader import *
from union_find import UnionFind


def get_data():
    lines = list(map(lambda s: s.split(), read_input(FilePath.CLUSTERING_BITS)))
    num_nodes = int(lines[0][0])
    nodes = dict()

    for i in range(1, len(lines)):
        node = ''.join(lines[i])
        nodes[node] = nodes.get(node, []) + [i]

    return nodes, num_nodes


def bit_shift(bit):
    return '0' if int(bit) else '1'


def get_one_bit_candidates(node, g):
    candidates = []
    for i in range(len(node)):
        change_to = bit_shift(node[i])
        candidate = node[:i] + change_to + node[i+1:]
        candidate_index = g.get(candidate, None)

        if candidate_index is not None:
            candidates += candidate_index

    return candidates


def get_two_bit_candidates(node, g):
    candidates = []

    for i in range(len(node)):
        first_bit_change_to = bit_shift(node[i])
        node_first_bit_changed = node[:i] + first_bit_change_to + node[i+1:]
        for j in range(i + 1, len(node)):
            second_bit_change_to = bit_shift(node[j])
            candidate = node_first_bit_changed[:j] + second_bit_change_to + node_first_bit_changed[j+1:]
            candidate_index = g.get(candidate, None)

            if candidate_index is not None:
                candidates += candidate_index

    return candidates


def clustering(nodes, num_nodes):
    uf = UnionFind(num_nodes)

    for node in nodes.keys():
        us = nodes.get(node)

        one_bit_candidates = get_one_bit_candidates(node, nodes)
        two_bit_candidates = get_two_bit_candidates(node, nodes)
        candidates = one_bit_candidates + two_bit_candidates

        if len(us) > 1:
            for i in range(len(us)):
                for j in range(i + 1, len(us)):
                    uf.union(us[i], us[j])

        for v in candidates:
            uf.union(us[0], v)

    return uf.size()


nodes, num_nodes = get_data()

max_distance = clustering(nodes, num_nodes)

print('Clustering bit max distance:', max_distance)  # 6118

