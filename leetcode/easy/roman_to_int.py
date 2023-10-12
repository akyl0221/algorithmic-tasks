class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        repeated = ("I", "X", "C", "M")
        for i in range(len(s) - 1, -1, -1):
            if d[s[i]] < result:
                if s[i] in repeated and d[s[i]] * 3 > result:
                    result += d[s[i]]
                else:
                    result -= d[s[i]]
            else:
                result += d[s[i]]
        return result
