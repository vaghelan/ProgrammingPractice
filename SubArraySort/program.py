def subarraySort(array):
    # Write your code here.
    left = -1
    right = -1

    for i in range(0, len(array)):

        if i < len(array) - 1 and array[i] > array[i+1]:
            if left == -1:
                left = i

            right = i

        if i > 0 and array[i] < array[i - 1]:
            if left == -1:
                left = i - 1

            right = i


    if left == -1:
        return [-1, -1]

    # find min and max
    min_subarray = array[left]
    max_subarray = array[right]
    for i in range(left, right+1):
        if array[i] < min_subarray:
            min_subarray = array[i]

        if array[i] > max_subarray:
            max_subarray = array[i]


    # position min an max into the array

    for i in  range(0, left):
        if min_subarray < array[i]:
            left = i
            break

    for i in range(len(array) - 1, right, -1):
        if max_subarray > array[i]:
            right = i
            break

    return [left, right]