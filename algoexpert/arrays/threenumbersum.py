"""https://www.algoexpert.io/questions/three-number-sum"""

def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    for i in range(len(array)):
        tmp = targetSum - array[i]
        for j in range(i + 1, len(array)):
            if tmp - array[j] in array[j:] and tmp - array[j] > array[j]:
                res.append([array[i], array[j], tmp - array[j]])
    return res
