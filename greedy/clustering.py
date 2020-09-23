import sys
sys.path.append("..")

from utils.file_reader import *
from union_find import UnionFind


def get_data():

    lines = list(map(lambda s: s.split(), read_input(FilePath.CLUSTERING)))
    num_nodes = int(lines[0][0])
    g = []

    for line in lines[1:]:
        u, v, cost = map(int, line)
        g.append((cost, u, v))

    return g, num_nodes


def clustering(g, num_nodes, k):
    different_clusters, index = [], 0
    g.sort()
    uf = UnionFind(num_nodes)

    while uf.size() > k:
        cost, u, v = g[index]
        uf.union(u, v)
        index+=1

    for cost, u, v, in g:
        u_leader, v_leader = uf.find(u), uf.find(v)
        if u_leader != v_leader:
            different_clusters.append(cost)

    return min(different_clusters)


g, num_nodes = get_data()

max_distance = clustering(g, num_nodes, 4)

print('Clustering max distance:', max_distance)