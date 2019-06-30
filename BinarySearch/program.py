def binarySearch(array, target):
    # Write your code here.
    n = len(array)
    start = 0
    end = n - 1

    c = 1

    while (start <= end):

        #print (c, start, end, array[start:end+1])
        c += 1
        mid = int(start + (end - start) / 2)
        #print ("----", mid)

        if target == array[mid]:
            return mid

        if target < array[mid]:
            end = mid - 1
            continue

        start = mid+1
        #print(c, start, end)

    return -1
