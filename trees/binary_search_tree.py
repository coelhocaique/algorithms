import math

"""
    Implementation of a binary search tree and operations
    
    The tree is implemented as a dictionary where the key are the indexes of the tree nodes
    
    The indexes are calculated using the formula 2*i for left leaf and 2*i+1 for the right leaf 
"""


class BinarySearchTree:

    def __init__(self):
        self.__tree = dict()
        self.highest_index = 0

    """
        Returns the root of the tree (index, node), if it is initialized else None
    """
    def root(self):
        return 1, self.__tree.get(1, None)

    """
        Returns the left leaf of the node index informed it is present
    """
    def left(self, index):
        return index * 2, self.__tree.get(index * 2, None)

    """
        Returns the right leaf of the node index informed it is present
    """
    def right(self, index):
        return index * 2 + 1, self.__tree.get(index * 2 + 1, None)

    """
        Returns the parent of the node index informed 
    """
    def parent(self, index):
        return index // 2, self.__tree.get(index // 2, None)

    """
        Returns the height of the tree
    """
    def tree_height(self):
        return int(math.log2(self.highest_index))

    """
        Searches the element in the three, returns index, node if it is found
    """
    def search(self, element, insertion=False, element_comparator='>='):
        index, node = self.root()

        while node is not None and (insertion or node != element):
            if eval(str(element) + element_comparator + str(node)):
                index, node = self.right(index)
            else:
                index, node = self.left(index)

        return index, node

    """
        Inserts an element in the tree
    """
    def insert(self, element):
        index, node = self.search(element, True)
        self.__tree[index] = element
        self.highest_index = max(self.highest_index, index)

    """
        Finds the minimum element of the tree 
    """
    def min_element(self):
        index, node = self.root()
        min_node = node

        while node is not None:
            index, node = self.left(index)
            if node is not None:
                min_node = node

        return min_node

    """
        Finds the maximum element of the tree
    """
    def max_element(self):
        index, node = self.root()
        max_node = node

        while node is not None:
            index, node = self.right(index)
            if node is not None:
                max_node = node

        return max_node

    """
       Recursive function to compute predecessor
    """
    def __predecessor__(self, index):
        if index % 2 > 0:
            return self.parent(index)

        return self.__predecessor__(self.parent(index)[0])

    """
       Finds the predecessor of the element informed
       Predecessor is the first node smaller than the informed element
    """
    def predecessor(self, element):
        index, node = self.search(element, True, '>')
        return self.__predecessor__(index)

    """
        Recursive function to compute successor
    """
    def __successor__(self, index):
        if index % 2 == 0:
            return self.parent(index)

        return self.__successor__(self.parent(index)[0])

    """
       Finds the successor of the element informed
       Successor is the first node greater than the informed element 
    """
    def successor(self, element):
        index, node = self.search(element, True)
        return self.__successor__(index)

    """
        Recursive function to in-order traversal
    """
    def __in_order_traversal__(self, index, node, traversal):
        left_index, left_node = self.left(index)

        if left_node is not None:
            self.__in_order_traversal__(left_index, left_node, traversal)

        traversal += [node]

        right_index, right_node = self.right(index)

        if right_node is not None:
            self.__in_order_traversal__(right_index, right_node, traversal)

        return traversal

    """
        Returns all the nodes in the three ordered
    """
    def in_order_traversal(self):
        index, node = self.root()
        return self.__in_order_traversal__(index, node, []) if node else []

    """
        Recursive function to delete
        If the queried node has only right child, finds its successor and replaces with node
        If the queried node has both or only left child, finds its predecessor and replaces with node
        Do it until the end of the three is reached    
    """
    def __delete__(self, index, node):
        if node:
            left_index, left_node = self.left(index)
            right_index, right_node = self.right(index)

            if right_node is not None or left_node is not None:
                if right_node is not None and left_node is None:
                    next_index, next_node = self.successor(node)
                else:
                    next_index, next_node = self.predecessor(node)

                self.__tree[index] = next_node
                self.__delete__(next_index, next_node)
            else:
                self.__tree.pop(index)

    """
        Deletes a node of the tree, if it is present
    """
    def delete(self, element):
        index, node = self.search(element)
        self.__delete__(index, node)
        print('delete node:', element, 'tree:', self.__tree)

    """
        Recursive function to compute rank operation
    """
    def __rank__(self, index, node, element, rank):
        if len(rank) >= element:
            return rank

        left_index, left_node = self.left(index)

        if left_node is not None:
            self.__rank__(left_index, left_node, element, rank)

        if node <= element:
            rank += [node]

        right_index, right_node = self.right(index)

        if right_node is not None:
            self.__rank__(right_index, right_node, element, rank)

        return rank

    """
        Returns all the element in the three less than or equal the informed element    
    """
    def rank(self, element):
        index, node = self.root()
        return self.__rank__(index, node, element, []) if node else []

    """
        Recursive function to compute selection operation
    """
    def __selection__(self, index, node, order_statistic, selection):
        if len(selection) >= order_statistic:
            return selection

        left_index, left_node = self.left(index)

        if left_node is not None:
            self.__selection__(left_index, left_node, selection)

        selection += [node]

        right_index, right_node = self.right(index)

        if right_node is not None:
            self.__selection__(right_index, right_node, selection)

        return selection

    """
        Returns the order_statistic smallest element of the three
    """
    def selection(self, order_statistic):
        index, node = self.root()
        if node is not None:
            selection = self.__selection__(index, node, order_statistic, [])
            if len(selection) >= order_statistic:
                return selection[order_statistic - 1]


bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(9)
bst.insert(14)
bst.insert(18)
bst.insert(1)
bst.insert(4)
bst.insert(7)
bst.insert(11)
bst.insert(16)
bst.insert(25)


print('search 5:', bst.search(5))                  # (3, 5)
print('tree height:', bst.tree_height())           # 2
print('min element:', bst.min_element())           # 1
print('max element:', bst.max_element())           # 5
print('predecessor of 5:', bst.predecessor(5))     # (3, 5)
print('successor of 2:', bst.successor(2))         # (1, 3)
print('in order traversal=', bst.in_order_traversal())
print('rank=', bst.rank(12))
print('selection 10th order statistic=', bst.selection(10))
print('deleting root')
bst.delete(10)

print('search 5:', bst.search(5))                  # (3, 5)
print('tree height:', bst.tree_height())           # 2
print('min element:', bst.min_element())           # 1
print('max element:', bst.max_element())           # 5
print('predecessor of 5:', bst.predecessor(5))     # (3, 5)
print('successor of 2:', bst.successor(2))         # (1, 3)
print('in order traversal=', bst.in_order_traversal())
print('rank=', bst.rank(12))
print('selection 10th order statistic=', bst.selection(10))




