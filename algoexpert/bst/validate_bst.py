"""https://www.algoexpert.io/questions/validate-bst"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, max_value=None, min_value=None):
    if tree is None:
        return True

    if tree.left:
        if (
                tree.value < tree.left.value or
                (max_value is not None and tree.left.value >= max_value) or
                (min_value is not None and tree.left.value < min_value)
        ):
            return False

    if tree.right:
        if (
                tree.value > tree.right.value or
                (max_value is not None and tree.right.value >= max_value) or
                (min_value is not None and tree.right.value < min_value)
        ):
            return False

    left = validateBst(tree.left, max_value=tree.value, min_value=min_value)
    right = validateBst(tree.right, max_value=max_value, min_value=tree.value)

    return left and right