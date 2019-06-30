def validateBst(tree, min_range=float("-inf"), max_range=float("inf")):
    # Write your code here.
    if tree == None:
        return True


    if tree.value >= min_range and tree.value < max_range:

        is_left_valid = validateBst(tree.left, min_range, tree.value)

        return is_left_valid and validateBst(tree.right, tree.value, max_range)

    return False