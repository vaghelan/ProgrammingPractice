def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    max  = 0

    for i in range(len(array)):
        new_max = 0
        for j in range(i, len(array), 2):
            new_max = new_max + array[j]

        if new_max > max:
            max = new_max

    return max