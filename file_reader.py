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


def get_input_as_list(filename):
    output = []
    file = open(os.path.abspath('data') + filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        output.append(int(line))

    return output


def get_dict_as_adj_list(filename):
    adj_list = dict()
    lines = read_file(filename)

    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    lines = map(lambda s: s.split(' '), lines)

    for line in lines:
        adj_list[int(line[0])] = list(map(lambda s: int(s), line[1:]))

    return adj_list


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


def read_dijkstra_input(filename):
    lines = read_file(filename)
    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    lines = map(lambda s: s.split(' '), lines)
    return lines

