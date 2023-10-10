"""https://leetcode.com/problems/excel-sheet-column-title/"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber > 26:
            tmp = columnNumber % 26
            columnNumber = columnNumber // 26
            if tmp != 0:
                s = chr(64 + tmp) + s
            else:
                s = chr(64 + 26) + s
                columnNumber -= 1
        if columnNumber != 0:
            s = chr(64 + columnNumber) + s
        return s
