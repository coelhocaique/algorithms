import os
import re


class FilePath:
    INVERSIONS = '/inversions.txt'
    COMPARISONS = '/comparisons.txt'
    MIN_CUT = '/min_cut.txt'
    SCC = '/scc.txt'
    DIJKSTRA = '/dijkstra.txt'


def read_file(filename):
    f = open(os.path.abspath('data') + filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_input(filename):
    lines = read_file(filename)
    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    return lines


def read_scc_input(filename):
    g, g_inverted = {}, {}
    nodes = set()

    lines = map(lambda s: s.strip().split(), read_file(filename))

    for line in lines:
        src = int(line[0])
        dst = int(line[1])

        if src in g.keys():
            g.get(src).append(dst)
        else:
            g[src] = [dst]

        if dst in g_inverted.keys():
            g_inverted.get(dst).append(src)
        else:
            g_inverted[dst] = [src]

        nodes.add(src)
        nodes.add(dst)

    return g, g_inverted, len(nodes)

