"""https://leetcode.com/problems/day-of-the-year/submissions/1074946763/"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')
        if int(year) % 4 == 0 and int(year) % 100 != 0:
            leap = True
        elif int(year) % 400 == 0:
            leap = True
        else:
            leap = False

        d_m = {
            1: 31,
            2: 29 if leap else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

        cur_day = int(day)
        for i in range(1, int(month)):
            cur_day += d_m[i]
        return cur_day