def maxSubsetSumNoAdjacent(array):
    # Write your code here.

    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    maxSum = array[0]

    if len(array) >= 2:
        maxSum = max(array[0], array[1])

    first = array[0]
    second = maxSum

    for i in range(2, len(array)):
        maxSum = max(first+array[i], second)
        first = second
        second = maxSum

    return maxSum

