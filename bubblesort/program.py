def bubbleSort(array):
    # Write your code here.
    isSorted = False

    counter = 0

    while not isSorted:

        isSorted = True

        for i in range(len(array) - (counter + 1)):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False

        counter += 1
    return array

