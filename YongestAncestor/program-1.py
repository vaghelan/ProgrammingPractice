def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    descendantOneLineage = []


    descendantOneLineage.append(descendantOne)
    p = descendantOne

    s = p.name
    while p.ancestor != None:
        descendantOneLineage.append(p.ancestor)
        s = s + p.ancestor.name
        if descendantOne.ancestor.name == "A":
            break

        p = p.ancestor



    descendantTwoLineage = []

    descendantTwoLineage.append(descendantTwo)
    p = descendantTwo

    s = p.name
    while p.ancestor != None:
        descendantTwoLineage.append(p.ancestor)
        s = s + p.ancestor.name
        if descendantTwo.ancestor.name == "A":
              break
        p = p.ancestor


    p = len(descendantOneLineage) - 1
    q = len(descendantTwoLineage) - 1

    potentialCandidate = None


    while p >= 0 and q >= 0:
        #print(" p and q ", p, q, descendantOneLineage[p].name, descendantTwoLineage[q].name)
        if descendantOneLineage[p].name == descendantTwoLineage[q].name:
            potentialCandidate = descendantOneLineage[p]
            p -= 1
            q -= 1
        else:
            break

    #print ("Result = ", potentialCandidate.name)
    return potentialCandidate
