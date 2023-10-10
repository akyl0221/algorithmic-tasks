"""https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/"""
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        for _ in range(3):
            mat = self.rotate(mat)
            if mat == target:
                return True
        return False

    def rotate(self, mat: List[List[int]]):
        transposed = []
        for row in zip(*mat):
            transposed.append(list(row))
        rotated = []
        for row in transposed:
            rotated.append(row[::-1])
        return rotated
