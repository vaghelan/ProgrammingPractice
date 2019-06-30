def maxPathSum(tree):
    # Write your code here.
    if tree is None:
        return 0



    leftSum = maxPathSum(tree.left)
    rightSum = maxPathSum(tree.right)

    temp = max (leftSum +  tree.value, tree.value)
    maxSum = max (rightSum + temp, temp)


    return maxSum