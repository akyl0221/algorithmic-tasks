"""https://www.algoexpert.io/questions/sorted-squared-array"""

def sortedSquaredArray(array):
    # Write your code here.
    arr = [0] * len(array)
    left = 0
    i = right = len(array) - 1

    while right >= left:
        if abs(array[left]) > abs(array[right]):
            arr[i] = array[left] ** 2
            left += 1
        else:
            arr[i] = array[right] ** 2
            right -= 1
        i -= 1

    return arr
