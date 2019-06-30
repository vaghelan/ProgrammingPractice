# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
import math
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.count = 0
        self.buildHeap(array)


    def buildHeap(self, array):
        # Write your code here.
        self.heap = []

        for i in array:
            self.insert(i)

    def siftDown(self):
        # Write your code here.
        parent = 0
        c1 = parent*2 + 1
        c2 = c1 + 1

        while c1 <= self.count - 1 or c2 <= self.count - 1:
            min_index = c2
            if c2 <= self.count - 1:
                if self.heap[c1] < self.heap[c2]:
                    min_index = c1
            else:
                min_index = c1

            if self.heap[min_index] < self.heap[parent]:
                self.heap[min_index], self.heap[parent] = self.heap[parent], self.heap[min_index]
                parent = min_index
                c1 = parent * 2 + 1
                c2 = c1 + 1
            else:
                return


    def siftUp(self):
        # Write your code here.
        child = self.count - 1
        parent = int(math.floor((child-1)/2))

        while (child > 0):
            if self.heap[child] < self.heap[parent] :
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
                parent = int(math.floor((child-1)/2))
            else:
                break

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.

        if self.count == 0:
            return


        h = self.heap[0]
        self.heap[0] = self.heap.pop()


        self.count -= 1

        self.siftDown()


    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.count += 1
        self.siftUp()
