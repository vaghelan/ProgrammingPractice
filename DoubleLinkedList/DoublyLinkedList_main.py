# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def increment(self):
        self.num += 1

    def decrement(self):
        self.num -= 1

    def getcount(self):
        return self.num


    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            self.increment()
            return

        self.insertBefore(self.head, node)


    def setTail(self, node):
        # Write your code here.

        if self.tail is None:
            self.head = node
            self.tail = node
            self.increment()
            return
        self.insertAfter(self.tail, node)


    def insertBefore(self, node, nodeToInsert):
        # Write your code here

        if self.containsNodeWithValue(nodeToInsert.value):
            self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is not None:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

        if self.head is node:
            self.head = nodeToInsert

        self.increment()

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.

        if self.containsNodeWithValue(nodeToInsert.value):
            self.remove(nodeToInsert)

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is not None:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

        if self.tail is node:
            self.tail = nodeToInsert

        self.increment()

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.

        if self.containsNodeWithValue(nodeToInsert.value):
            self.remove(nodeToInsert)

        if position == 1:
            self.setHead(nodeToInsert)
            return


        t_pos = 1
        t = self.head

        while (t is not None and t_pos != position):
            if t_pos == position:
                break
            t = t.next
            t_pos = t_pos + 1

        if t is not None:
            self.insertAfter(t.prev, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.


        while (1):
            exit_me = True
            t = self.head
            while (t):
                if t.value == value:
                    print ("removed value = ", value)
                    self.remove(t)
                    exit_me = False
                    break
                t = t.next
            if exit_me == True:
                break

    def remove(self, node):
        # Write your code here.

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        node.prev = None
        node.next = None

        self.decrement()


    def containsNodeWithValue(self, value):
        # Write your code here.
        t = self.head
        while (t):
            if t.value == value:
                return True
            t = t.next

        return False


import DoublyLinkedList_main
import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def expectHeadTail(self, linkedList, head, tail):
  self.assertEqual(linkedList.head, head)
  self.assertEqual(linkedList.tail, tail)

def expectSingleNode(self, linkedList, node):
  self.assertEqual(linkedList.head, node)
  self.assertEqual(linkedList.tail, node)

def getNodeValuesHeadToTail(linkedList):
  values = []
  node = linkedList.head
  while node is not None:
    values.append(node.value)
    node = node.next
  return values


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values

def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values

def removeNodes(linkedList, nodes):
    for node in nodes:
        linkedList.remove(node)
