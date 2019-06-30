def twoNumberSum(array, targetSum):
    # Write your code here.
    target_num = {}
    for a in array:

        other = targetSum - a

        if other in target_num:
            if other > a:
                return [a, other ]
            return [other, a]


        target_num[a] = True
        print (target_num)

    return []



print (twoNumberSum([4, 6, 1], 5))