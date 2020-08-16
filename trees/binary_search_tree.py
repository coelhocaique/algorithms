import math


class BST:
    def __init__(self):
        self.queue = dict()
        self.highest_index = 0

    def root(self):
        return 1, self.queue.get(1, None)

    def left(self, index):
        return index * 2, self.queue.get(index * 2, None)

    def right(self, index):
        return index * 2 + 1, self.queue.get(index * 2 + 1, None)

    def parent(self, index):
        return index // 2, self.queue.get(index // 2, None)

    def tree_height(self):
        return int(math.log2(self.highest_index))

    def search(self, element, insertion=False):
        index, node = self.root()

        while node and (insertion or node != element):
            if element >= node:
                index, node = self.right(index)
            else:
                index, node = self.left(index)

        return index, node

    def insert(self, element):
        index, node = self.search(element, True)
        self.queue[index] = element
        self.highest_index = max(self.highest_index, index)

    def min_element(self):
        index, node = self.root()
        min_node = node

        while node:
            index, node = self.left(index)
            if node:
                min_node = node

        return min_node

    def max_element(self):
        index, node = self.root()
        max_node = node

        while node:
            index, node = self.right(index)
            if node:
                max_node = node

        return max_node

    def __predecessor_recur(self, index):
        if index % 2 > 0:
            return self.parent(index)

        return self.__predecessor_recur(self.parent(index)[0])

    def predecessor(self, element):
        index, node = self.search(element)

        if node:
            left_index, left_node = self.left(index)

            if left_node:
                return left_index, left_node

        return self.__predecessor_recur(index)

    def __successor_recur(self, index):
        if index % 2 == 0:
            return self.parent(index)

        return self.__successor_recur(self.parent(index)[0])

    def successor(self, element):
        index, node = self.search(element, True)
        return self.__successor_recur(index)

    def __in_order_traversal_recur(self, index, node):
        left_index, left_node = self.left(index)

        if left_node:
            self.__in_order_traversal_recur(left_index, left_node)

        print(node)

        right_index, right_node = self.right(index)

        if right_node:
            self.__in_order_traversal_recur(right_index, right_node)

    def in_order_traversal(self):
        index, node = self.root()
        if node:
            self.__in_order_traversal_recur(index, node)

    def delete(self, element):
        pass


bst = BST()

bst.insert(3)
bst.insert(1)
bst.insert(2)
bst.insert(5)
bst.insert(4)

print('search 5: ', bst.search(5))                  # (3, 5)
print('tree height: ', bst.tree_height())           # 2
print('min element: ', bst.min_element())           # 1
print('max element: ', bst.max_element())           # 1
print('predecessor of 10: ', bst.predecessor(10))   # 5
print('successor of 2: ', bst.successor(2))         # 3
print('in order traversal')

bst.in_order_traversal()

# bst = BST()
#
# print()
# bst.insert(5)
# bst.insert(4)
# bst.insert(3)
# bst.insert(2)
# bst.insert(1)
#
# bst.in_order_traversal()


# print(bst.successor(5))
# print(bst.successor(4))
# print(bst.successor(3))
# print(bst.successor(2))
# print(bst.successor(1))







