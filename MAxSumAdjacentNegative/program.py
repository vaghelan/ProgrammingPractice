
def kadanesAlgorithm(array):
    # Write your code here.

    max_sum = array[0]
    peak = max_sum

    for i in range(1, len(array)):
        max_sum = max(max_sum + array[i], array[i])
        peak = max(peak, max_sum)

    return peak

