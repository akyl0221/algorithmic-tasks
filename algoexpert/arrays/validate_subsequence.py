"""https://www.algoexpert.io/questions/validate-subsequence"""

def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False
    arr_index = 0
    for i in range(len(sequence)):
        flag = False
        while arr_index < len(array):
            if sequence[i] == array[arr_index]:
                flag = True
                arr_index += 1
                break
            arr_index += 1
        if not flag:
            return False
    return True
