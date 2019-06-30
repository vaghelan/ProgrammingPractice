

def threeNumberSumV1(array, targetSum):
    # Write your code here.
    triplets = {}
    for i in range(0, len(array) - 2):
        for j in range(i+1, len(array) - 1):
            #if i == j:
            #    continue
            for k in range(j+1, len(array)):
             #   if k == i or k == j:
             #       continue
                if (array[i] + array[j] + array[k]) == targetSum:
                    a = [array[i], array[j], array[k]]
                    a.sort()
                    triplets[(a[0], a[1], a[2])] = True

    print(triplets)

    triplets_array = []
    for t in triplets:
        triplets_array.append([t[0], t[1], t[2]])
    return (triplets_array)


def threeNumberSum(array, targetSum):
    # Write your code here.
    triplets = []
    array.sort()

    for i in range(0, len(array) - 2):

        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left +=1
            else:
                right -= 1


    return (triplets)