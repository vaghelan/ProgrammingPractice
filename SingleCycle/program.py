def hasSingleCycle(array):

    currInx = 0

    numElementsVisited = 0

    while numElementsVisited < len(array):

        if numElementsVisited > 0 and currInx == 0:
            return False
    
        numElementsVisited += 1

        nextIdx = currInx + array[currInx]

        nextIdx = nextIdx % len(array)

        currInx = nextIdx if nextIdx >= 0 else len(array) + nextIdx

    return currInx == 0

