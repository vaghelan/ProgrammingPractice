# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearchXXX(self, array):
        # Write your code here.

        tmp = []

        tmp.append(self)

        while len(tmp) > 0:
            n = tmp.pop(0)

            array.append(n.name)

            for c in n.children:
                tmp.append(c)

        return array

    def breadthFirstSearch(self, array):
        # Write your code here.

        array.append(self)
        i = 0

        while i <= len(array) - 1:
            for c in array[i].children:
                array.append(c)
            array[i] = array[i].name
            i = i + 1

        return array