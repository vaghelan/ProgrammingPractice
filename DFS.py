# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearchBackend(self, array, visited):
            # Write your code here.
            array.append(self.name)
            visited[self.name] = None
            #print(visited)
            for v in self.children:
                if v.name not in visited:
                    v.depthFirstSearchBackend(array, visited)
            return array

    def depthFirstSearch(self, array):
        # Write your code here.
        visited = {}
        return self.depthFirstSearchBackend(array, visited)



test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = Node("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")


test5 = Node("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")

nodes = [test1, test2, test3, test4, test5]
for n in nodes:
    print (n.depthFirstSearch([]))
