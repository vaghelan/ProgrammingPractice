class top3:
    def __init__(self):
        self.smallest = None
        self.middle = None
        self.largest = None



    def insert(self, n):
        if self.largest  == None:
            self.largest = n
            return

        if n > self.largest:
            self.smallest = self.middle
            self.middle = self.largest
            self.largest = n
            return

        if self.middle == None:
            self.middle = n
            return

        if n > self.middle:
            self.smallest = self.middle
            self.middle = n
            return

        if self.smallest == None:
            self.smallest = n
            return

        if n > self.smallest:
            self.smallest = n
            return




def findThreeLargestNumbers(array):
    # Write your code here.
    h = top3()
    for i in array:
        h.insert(i)

    return [ h.smallest, h.middle, h.largest ]