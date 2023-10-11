import itertools
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for Hs in range(0, min(turnedOn, 4) + 1):
            Ms = turnedOn - Hs
            if not 0 <= Ms <= 6: continue
            hcomb = itertools.combinations(range(4), Hs)
            mcomb = itertools.combinations(range(6), Ms)
            hcomb = tuple(map(lambda hs: sum(2 ** i for i in hs), hcomb))
            mcomb = tuple(map(lambda ms: sum(2 ** i for i in ms), mcomb))
            res += ['{}:{:02d}'.format(h, m) for h in hcomb
                    for m in mcomb if h < 12 and m < 60]
        return res