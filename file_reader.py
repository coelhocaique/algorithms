import os
import re


class FilePath:
    INVERSIONS = '/inversions.txt'
    COMPARISONS = '/comparisons.txt'
    MIN_CUT = '/min_cut.txt'


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
    file = open(os.path.abspath('data') + filename, 'r')
    lines = file.readlines()
    file.close()

    lines = map(lambda s: re.sub('\s+', ' ', str(s.strip('\r\n'))).strip(), lines)
    lines = map(lambda s: s.split(' '), lines)

    for line in lines:
        adj_list[int(line[0])] = list(map(lambda s: int(s), line[1:]))

    return adj_list
