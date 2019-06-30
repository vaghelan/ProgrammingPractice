def fourNumberSum(array, targetSum):
    # Write your code here.

    pairs = {}

    quadruplets = []

    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            pair_sum = array[i] + array[j]

            candidate = targetSum - pair_sum

            if candidate in pairs:
                for pair in pairs[candidate]:
                    quadruplets.append([pair[0], pair[1], array[i], array[j]])


        for k in range(0, i):
            pair_sum = array[i] + array[k]

            if pair_sum not in pairs:
                pairs[pair_sum] = [[array[k], array[i]]]
            else:
                pairs[pair_sum].append([array[k], array[i]])


    return quadruplets