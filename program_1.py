import math
def findClosestValueInBst(tree, target):
    # Write your code here.

    closest = 99999

    t = tree

    while t != None:

        if math.fabs(t.value - target) < math.fabs(closest - target):
            closest = t.value

        if target > t.value:
            t = t.right
            continue

        t = t.left


    return closest