class heapd:
    def __init__(self, mode="min"):
        self.array = []
        self.array.append(0)
        self.count = 0
        self.mode = mode

    def insert(self, n):
        self.array.append(n)
        self.count += 1
        self.__percolate_up__()

    def __percolate_up__(self):
        if self.count < 2:
            return

        child = self.count
        parent = int(child/2)

        while (parent != 0):


            if (self.mode == "min" and self.array[parent] > self.array[child]) or (self.mode == "max" and self.array[parent] < self.array[child]):
                self.array[parent], self.array[child] = self.array[child], self.array[parent]
                child = parent
                parent = int(child / 2)
                continue
            break

    def get_top_3(self):
        if self.count < 3:
            return None
        if self.mode == "min" and self.array[2] > self.array[3]:
            self.array[2], self.array[3] = self.array[3], self.array[2]
        if self.mode == "max" and self.array[2] < self.array[3]:
            self.array[2], self.array[3] = self.array[3], self.array[2]

        return [self.array[3], self.array[2], self.array[1]]


def findThreeLargestNumbers(array):
    # Write your code here.
    h = heapd("max")
    for i in array:
        h.insert(i)

    return h.get_top_3()