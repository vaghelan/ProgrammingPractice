def invertBinaryTree(tree):
    # Write your code here.
    if tree == None:
        return

    invertBinaryTree(tree.left)

    invertBinaryTree(tree.right)

    tree.left, tree.right = tree.right, tree.left

    return