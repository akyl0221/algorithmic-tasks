"""https://leetcode.com/problems/flipping-an-image/description/"""
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            r = 0
            l = len(row) - 1
            while r < l:
                temp = self.invert_value(row[r])
                row[r] = self.invert_value(row[l])
                row[l] = temp
                r += 1
                l -= 1
            if len(row) % 2 == 1 and r == l:
                row[l] = self.invert_value(row[l])

        return image

    def invert_value(self, v: int) -> int:
        return 0 if v == 1 else 1