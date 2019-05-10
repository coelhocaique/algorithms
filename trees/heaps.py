
class PriorityQueue:
    def __init__(self, mode):
        self.__queue = []
        self.__comp = '<' if mode == 'min' else '>'

    def __eval(self, a, b):
        return eval('%d %s %d' % (a, self.__comp, b))

    def add(self, e):
        def bubble_up():
            size = self.size()
            if size > 1:
                index = size
                last_index = index
                new = self.get(index)
                while index > 1:
                    index = index // 2
                    parent = self.get(index)
                    if self.__eval(new, parent):
                        self.set(index, new)
                        self.set(last_index, parent)
                        last_index = index
                    else:
                        index = 0

        self.__queue.append(e)
        bubble_up()

    def poll(self):
        def choose_best_child(index, size):
            left_child_index = 2 * index
            right_child_index = left_child_index + 1
            left_child = self.get(left_child_index)
            right_child = self.get(right_child_index) if right_child_index <= size else None

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
                    child = self.get(best_child_index)

                    if self.__eval(child, new):
                        self.set(index, child)
                        self.set(best_child_index, new)
                        new = child
                        index = best_child_index
                    else:
                        index = size + 1

        e = self.peek()
        self.set(1, self.peek_last())
        del self.__queue[-1]
        bubble_down()
        return e

    def peek(self):
        if self.size() <= 0:
            raise ValueError('The queue is empty!')
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

    def set(self, index, value):
        self.__queue[index-1] = value

    def get(self, index):
        return self.__queue[index-1]

    def peek_last(self):
        return self.get(0)

    def __str__(self):
        return ','.join([str(e) for e in self.queue])


pq = PriorityQueue(mode='max')
pq.add(3)
pq.add(4)
pq.add(1)
pq.add(0)
pq.add(1)
pq.add(5)
print(pq.poll())
print(pq.poll())
print(pq.poll())
print(pq.poll())
print(pq.poll())
print(pq.poll())