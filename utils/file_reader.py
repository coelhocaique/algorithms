import os, re

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
    ALL_PAIRS_SHORTEST_PATH_1 = '/all_pairs_shortest_path_1.txt'
    ALL_PAIRS_SHORTEST_PATH_2 = '/all_pairs_shortest_path_2.txt'
    ALL_PAIRS_SHORTEST_PATH_3 = '/all_pairs_shortest_path_3.txt'
    ALL_PAIRS_SHORTEST_PATH_LARGE = '/all_pairs_shortest_path_large.txt'
    ALL_PAIRS_SHORTEST_PATH_4 = '/all_pairs_shortest_path_4.txt'
    TSP = '/tsp.txt'
    TSP_HEURISTIC = '/tsp_heuristic.txt'
    TWO_SAT_1 = '/2sat1.txt'
    TWO_SAT_2 = '/2sat2.txt'
    TWO_SAT_3 = '/2sat3.txt'
    TWO_SAT_4 = '/2sat4.txt'
    TWO_SAT_5 = '/2sat5.txt'
    TWO_SAT_6 = '/2sat6.txt'
    TWO_SAT = '/2sat.txt'

def read_file(filename):
    f = open(os.path.abspath('../data') + filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_input(filename):
    lines = read_file(filename)
    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    return lines

