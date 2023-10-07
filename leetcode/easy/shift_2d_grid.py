"""https://leetcode.com/problems/shift-2d-grid/"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nRows, nCols = len(grid), len(grid[0])
        k %= nRows * nCols
        if k == 0: return grid

        n = nRows * nCols
        arr = [0] * n
        for i in range(n):
            idx = (i + n - k) % n
            arr[i] = grid[idx // nCols][idx % nCols]

        for i in range(len(arr)):
            grid[i // nCols][i % nCols] = arr[i]
        return grid