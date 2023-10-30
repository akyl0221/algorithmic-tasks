"""https://www.algoexpert.io/questions/transpose-matrix """

def transposeMatrix(matrix):
    res = []
    for i in range(len(matrix[0])):
        arr = []
        for j in range(len(matrix)):
            arr.append(matrix[j][i])
        res.append(arr)
    return res
