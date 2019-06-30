def insertionSort(array):
    # Write your code here.

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] > array[j - 1]:
                break
            swap(j, j - 1, array)

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]