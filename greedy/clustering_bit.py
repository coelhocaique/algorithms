import sys
sys.path.append("..")

"""
    In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

    The data set is below.
    
    
    The format is:
    
    [# of nodes] [# of bits for each node's label]
    
    [first bit of node 1] ... [last bit of node 1]
    
    [first bit of node 2] ... [last bit of node 2]
    
    ...
    
    For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.
    
    The distance between two nodes uu and vv in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. 
    For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).
    
    The question is: what is the largest value of kk such that there is a kk-clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?
    
    NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. 
    So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?
"""

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

