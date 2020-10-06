import sys
sys.path.append("..")

"""
    This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

    [number_of_nodes]
    
    [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
    
    [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
    
    ...
    
    There is one edge (i,j)(i,j) for each choice of 1 \leq i \lt j \leq n1≤i<j≤n, where nn is the number of nodes.
    
    For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, 
    but you should NOT assume that they are distinct.
    
    Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kk of clusters is set to 4. What is the maximum spacing of a 4-clustering?
    
    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

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