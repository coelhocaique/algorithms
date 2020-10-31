import os
import re


class FilePath:
    INVERSIONS = '/inversions.txt'
    COMPARISONS = '/comparisons.txt'
    MIN_CUT = '/min_cut.txt'
    SCC = '/scc.txt'
    DIJKSTRA = '/dijkstra.txt'
    MEDIAN_MAINTENANCE = '/median.txt'
    TWO_SUM = '/2sum.txt'
    JOBS = '/jobs.txt'
    MST_PRIM = '/edges.txt'
    CLUSTERING = '/clustering1.txt'
    CLUSTERING_BITS = '/clustering_bit.txt'
    HUFFMAN_CODING = '/huffman.txt'
    MWIS = '/mwis.txt'
    KNAPSACK1 = '/knapsack1.txt'
    KNAPSACK2 = '/knapsack2.txt'


def read_file(filename):
    f = open(os.path.abspath('../data') + filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_input(filename):
    lines = read_file(filename)
    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    return lines

