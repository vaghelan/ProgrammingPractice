# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class BinaryTree:
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, values, i = 0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i], current)
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i], current)
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)

test1 = BinaryTree(1)

test2 = BinaryTree(1).insert([2, 3, 4])

test3 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])

test4 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])

test5 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

test6 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test1, actualTestCallback)
        self.assertEqual(testArray, [1])

    def test_case_2(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test2, actualTestCallback)
        self.assertEqual(testArray, [4, 2, 1, 3])

    def test_case_3(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test3, actualTestCallback)
        self.assertEqual(testArray, [4, 2, 5, 1, 6, 3, 7])

    def test_case_4(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test4, actualTestCallback)
        self.assertEqual(testArray, [8, 4, 9, 2, 10, 5, 1, 6, 3, 7])

    def test_case_5(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test5, actualTestCallback)
        self.assertEqual(testArray, [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 7])

    def test_case_6(self):
        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        program.iterativeInOrderTraversal(test6, actualTestCallback)
        self.assertEqual(testArray, [16, 8, 17, 4, 18, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15])


if __name__ == "__main__":
	unittest.main()
