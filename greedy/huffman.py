import sys
sys.path.append("..")

from utils.file_reader import *
from queue import PriorityQueue


class Node:

    def __init__(self, weight, left=None, right=None, label=None):
        self.label = label
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return str((self.label, self.weight, self.left, self.right))


def get_data():
    lines = list(read_input(FilePath.HUFFMAN_CODING))
    pq = PriorityQueue()

    for symbol in range(1, len(lines)):
        weight = lines[symbol]
        node = Node(weight=int(weight), label=str(symbol))
        pq.put(node)

    return pq


def compute_min_depth(root, count=0):
    left_depth, right_depth = count, count

    if root.left is not None:
        left_depth = compute_min_depth(root.left, count + 1)
    if root.right is not None:
        right_depth = compute_min_depth(root.right, count + 1)

    return min(left_depth, right_depth)


def compute_max_depth(root, count=0):
    left_depth, right_depth = count, count

    if root.left is not None:
        left_depth = compute_max_depth(root.left, count + 1)
    if root.right is not None:
        right_depth = compute_max_depth(root.right, count + 1)

    return max(left_depth, right_depth)


def huffman_coding(pq):

    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        new_node = Node(weight=a.weight + b.weight, left=a, right=b, label=a.label + b.label)
        pq.put(new_node)

    root = pq.get()
    return compute_max_depth(root), compute_min_depth(root)


pq = get_data()

result = huffman_coding(pq)
print('Maximum length = %d' % result[0])
print('Maximum length = %d' % result[1])