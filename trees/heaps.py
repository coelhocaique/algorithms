class PriorityQueue:
    def __init__(self, mode):
        self.__queue = []
        self.__comp = '<' if mode == 'min' else '>'

    def __eval(self, a, b):
        return eval(str(a) + self.__comp + str(b))

    def __set(self, index, value):
        self.__queue[index-1] = value

    def __get(self, index):
        return self.__queue[index-1]

    def add(self, e):
        def bubble_up():
            size = self.size()
            if size > 1:
                index = size
                last_index = index
                new = self.__get(index)
                while index > 1:
                    index = index // 2
                    parent = self.__get(index)
                    if self.__eval(new, parent):
                        self.__set(index, new)
                        self.__set(last_index, parent)
                        last_index = index
                    else:
                        index = 0

        self.__queue.append(e)
        bubble_up()

    def poll(self):
        def choose_best_child(index, size):
            left_child_index = 2 * index
            right_child_index = left_child_index + 1
            left_child = self.__get(left_child_index)
            right_child = self.__get(right_child_index) if right_child_index <= size else None

            return right_child_index if right_child and self.__eval(right_child,left_child) else left_child_index

        def has_children(index):
            return 2 * index <= self.size()

        def bubble_down():
            size = self.size()
            if size > 0:
                new = self.peek()
                index = 1
                while has_children(index):
                    best_child_index = choose_best_child(index, size)
                    child = self.__get(best_child_index)

                    if self.__eval(child, new):
                        self.__set(index, child)
                        self.__set(best_child_index, new)
                        index = best_child_index
                    else:
                        index = size + 1

        def poll_and_delete():
            e = self.peek()
            self.__set(1, self.peek_last())
            del self.__queue[-1]
            return e
        
        e = poll_and_delete()
        bubble_down()
        return e

    def peek(self):
        if self.size() <= 0:
            raise ValueError('The queue is empty!')
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

    def peek_last(self):
        return self.__get(0)

    def __str__(self):
        return ','.join([str(e) for e in self.__queue])