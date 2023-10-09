"""https://leetcode.com/problems/matrix-diagonal-sum/"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = 0
        r = len(mat[0]) - 1
        row = 0
        if len(mat) == 1:
            return mat[0][0]

        d = len(mat[0])
        s = 0
        while row < d:
            if l == r:
                s += mat[row][l]
            else:
                s += (mat[row][l] + mat[row][r])
            print(mat[row][l], 'l')
            print(mat[row][r], 'r')

            row += 1
            r -= 1
            l += 1
        return s
