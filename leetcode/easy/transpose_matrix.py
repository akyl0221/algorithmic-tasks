from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []

        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(matrix[j][i])

            ans.append(arr)

        return ans
