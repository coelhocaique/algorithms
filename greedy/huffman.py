import sys
sys.path.append("..")

"""
    This file describes an instance of the problem. It has the following format:

    [number_of_symbols]
    
    [weight of symbol #1]
    
    [weight of symbol #2]
    
    ...
    
    For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A More Complex Example" video.)
    
    Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is the maximum length of a codeword in the resulting Huffman code?
    
    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
    
    Continuing the previous problem, what is the minimum length of a codeword in your Huffman code?
"""

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