"""https://leetcode.com/problems/image-smoother/submissions/1065040056/"""
from math import floor
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = 1
                tmp = img[i][j]
                right_corner = j + 1 < n
                down_corner = i + 1 < m
                left_corner = j - 1 > -1
                up_corner = i - 1 > -1

                if right_corner:
                    count += 1
                    tmp += img[i][j + 1]
                if left_corner:
                    count += 1
                    tmp += img[i][j - 1]
                if up_corner:
                    count += 1
                    tmp += img[i - 1][j]
                if down_corner:
                    count += 1
                    tmp += img[i + 1][j]

                if right_corner and down_corner:
                    count += 1
                    tmp += img[i + 1][j + 1]

                if right_corner and up_corner:
                    count += 1
                    tmp += img[i - 1][j + 1]

                if left_corner and up_corner:
                    count += 1
                    tmp += img[i - 1][j - 1]

                if left_corner and down_corner:
                    count += 1
                    tmp += img[i + 1][j - 1]

                res[i].append(floor(tmp / count))

        return res
