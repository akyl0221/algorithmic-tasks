"""https://www.algoexpert.io/questions/find-closest-value-in-bst"""


def findClosestValueInBst(tree, target, arr=None):
    # Write your code here.
    arr = arr or []
    arr.append(tree.value)
    if tree.value > target and tree.left:
        findClosestValueInBst(tree.left, target, arr)
    elif tree.value < target and tree.right:
        findClosestValueInBst(tree.right, target, arr)
    closest = arr[0]
    for i in arr:
        if abs(target - i) < abs(target - closest):
            closest = i

    return closest


def findClosestValueInBst(tree, target, closest = None):
    if closest is None or abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if tree.value > target and tree.left:
        return findClosestValueInBst(tree.left, target, closest)
    elif tree.value < target and tree.right:
        return findClosestValueInBst(tree.right, target, closest)
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
