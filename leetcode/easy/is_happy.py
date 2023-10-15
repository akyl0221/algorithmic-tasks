"""https://leetcode.com/problems/happy-number/description/"""

class Solution:
    def isHappy(self, n: int) -> bool:
        n_s = str(n)
        s = 0
        for i in n_s:
            s += int(i) ** 2

        if s == 1:
            return True

        if s in (2, 3, 4, 5, 6, 8, 9):
            return False

        return self.isHappy(s)
