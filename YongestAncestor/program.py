def findLevelOfANode(node, topAncestor):
    depth = 0

    while node != topAncestor:
        depth += 1
        node = node.ancestor

    depth += 1

    return depth

def backTrack(node, level):
    while level > 0:
        node = node.ancestor
        level = level - 1

    return node

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneLevel = findLevelOfANode(descendantOne, topAncestor)
    descendantTwoLevel = findLevelOfANode(descendantTwo, topAncestor)

    if descendantOneLevel > descendantTwoLevel:
        second = descendantTwo
        first = backTrack(descendantOne, descendantOneLevel - descendantTwoLevel)
    else:
        second = descendantOne
        first = backTrack(descendantTwo, descendantTwoLevel - descendantOneLevel)

    while first != second:
        first = first.ancestor
        second = second.ancestor

    return first
