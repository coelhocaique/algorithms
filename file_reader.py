import os


class FilePath:
    INVERSIONS = '/inversions.txt'
    COMPARISONS = '/comparisons.txt'


def get_input_as_list(filename):
    output = []
    file = open(os.path.abspath('data') + filename, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        output.append(int(line))

    return output
