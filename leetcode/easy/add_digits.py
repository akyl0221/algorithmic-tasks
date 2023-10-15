"""https://leetcode.com/problems/add-digits/description/"""


class Solution:
    def addDigits(self, num: int) -> int:
        num_s = str(num)
        s = 0
        for i in num_s:
            s += int(i)
        if s < 10:
            return s
        return self.addDigits(s)