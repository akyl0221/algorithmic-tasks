"""https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/"""
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = 0
        flag = True
        for i in range(len(matrix)):
            mins = min(matrix[i])

            index = matrix[i].index(mins)
            flag = True
            for j in range(len(matrix)):
                if j == i:
                    continue
                if matrix[j][index] > mins:
                    flag = False
                    break
            if flag:
                break

        return [mins] if flag else []
