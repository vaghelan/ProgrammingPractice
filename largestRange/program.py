def findRange(array, start):
#   find left side
    left  = start
    right = start

    num = start - 1

    while (True):
        if num in array:
            left = num
            num -= 1
        else:
            break

    num = start + 1

    while (True):
        if num in array:
            right = num
            num += 1
        else:
            break

    return (right - left + 1, (left, right))
#   find right side

def largestRange(array):
    # Write your code here.
    range = ( -1, (0, 0))
    nums = {}

    for i in array:
        nums[i] = True

    for i in array:
        if i in nums:
            if nums[i] == True:
                nums[i] = False

                result = findRange(array, i)
                if result[0] > range[0]:
                    range = result


    return [range[1][0], range[1][1]]
