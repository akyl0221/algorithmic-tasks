"""https://leetcode.com/problems/excel-sheet-column-number/"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0

        for i in range(len(columnTitle)):
            if i == len(columnTitle) - 1:
                column += (ord(columnTitle[i]) - 64)
            else:
                column += ((ord(columnTitle[i]) - 64) * (26**(len(columnTitle) - 1 - i)))
        return column
