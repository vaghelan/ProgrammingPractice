# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def insert__(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        next_node = self
        parent_node = None

        while (next_node != None):
            parent_node = next_node

            if value >= next_node.value:
                next_node = next_node.right
                continue

            next_node = next_node.left

        if value >= parent_node.value:
            parent_node.right = BST(value)
        else:
            parent_node.left = BST(value)

        return self

    def contains(self, value):
        # Write your code here.


        if self.value == value:
            return True

        if  value < self.value:
            if self.left != None:
                return self.left.contains(value)

        elif value > self.value:
            if self.right != None:
                return self.right.contains(value)

        return False

    def findNextInOrderNode(self):
        if self.right == None:
            return None, None, None

        minNode = self.right
        parent = self
        direction = 1

        while minNode.left != None:
            parent = minNode
            minNode = minNode.left
            direction = 0

        return minNode, parent, direction

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        next_node = self
        parent_node = None

        direction = 0

        while (next_node != None):


            if value > next_node.value:
                parent_node = next_node
                next_node = next_node.right
                direction = 1
                if next_node == None:
                    return self  # we did not find anything

                continue

            elif value < next_node.value:
                parent_node = next_node
                next_node = next_node.left
                direction = 2

                if next_node == None:
                    return self  # we did not find anything

                continue

            break

        # we found the node which we want to delete
        # we know its parent


        #Case 1
        # Node to be deleted is a leaf node

        if next_node.left == None and next_node.right == None:
            if direction == 1:
                parent_node.right = None
            elif direction == 2:
                parent_node.left = None

            return self

        # Case 2 :
        # Node to be deleted has only one child

        if next_node.left == None or next_node.right == None:


            if next_node.left != None: # node to be removed has left child
                if direction == 1: # it was right
                    parent_node.right = next_node.left
                elif direction == 2: # it was left
                    parent_node.left = next_node.left
                else:
                    return next_node.left

            elif next_node.right != None: # node to be removed has right child
                if direction == 1:
                    parent_node.right = next_node.right
                elif direction == 2:
                    parent_node.left = next_node.right
                else: # root node
                    return next_node.right

            return self

        #Case 3 :
        # Node to be deleted has two childrens


        minNode, its_parent, direction = next_node.findNextInOrderNode()

        if minNode == None:
            self.value = None
            self.left = None
            self.right = None
            return self

        # we have the parent of min node
        # we know what node to remove

        next_node.value = minNode.value

        if direction == 1:
            its_parent.right = minNode.right
        else:
            its_parent.left = minNode.right

        #minNode.right = parent_node

        #its_parent.remove(minNode.value)

        return self
