def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()


    i = 0
    j = 0

    min_sum = float('inf')
    current = float('inf')


    while (i < len(arrayOne) and (j < len(arrayTwo))):
        c_sum = abs(arrayOne[i] - arrayTwo[j])

        if c_sum == 0:
            return ([arrayOne[i], arrayTwo[j]])


        if c_sum < min_sum:
            min_sum = c_sum
            current = [ arrayOne[i], arrayTwo[j] ]

        if arrayOne[i] < arrayTwo[j]:
            i += 1
            continue

        j += 1

    return (current)
