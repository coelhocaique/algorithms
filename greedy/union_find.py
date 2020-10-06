import sys
sys.path.append("..")

"""
    Implementation of Union-Find with path compression and Union by Rank
"""


class UnionFind:

    def __init__(self, num_nodes):
        self.__ranks__= [0 for __ in range(num_nodes + 1)]
        self.__leaders__ = [x for x in range(num_nodes + 1)]
        self.__size__ = num_nodes

    def find(self, u):
        leader = self.__leaders__[u]
        if leader == u:
            return leader
        else:
            next_leader = self.find(leader)
            self.__leaders__[u] = next_leader  # path compression
            return next_leader

    def union(self, u, v):
        u_leader, v_leader = self.find(u), self.find(v)

        if u_leader == v_leader:
            return False

        u_rank, v_rank = self.__ranks__[u_leader], self.__ranks__[v_leader]

        if v_rank > u_rank:
            self.__leaders__[u_leader] = v_leader
        else:
            self.__leaders__[v_leader] = u_leader
            if u_rank == v_rank:
                self.__ranks__[u_leader]+=1

        self.__size__-=1
        return True

    def size(self):
        return self.__size__

    def leaders(self):
        return self.__leaders__
