"""https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a_moves = []
        b_moves = []
        for i in range(len(moves)):
            if (i + 1) % 2 == 1:
                a_moves.append(moves[i])
            else:
                b_moves.append(moves[i])

        if len(a_moves) < 3 and len(b_moves) < 3:
            return "Pending"

        for i, j in a_moves:
            if [i + 1, j] in a_moves and [i + 2, j] in a_moves:
                return "A"
            if [i, j + 1] in a_moves and [i, j + 2] in a_moves:
                return "A"
            if [i + 1, j + 1] in a_moves and [i + 2, j + 2] in a_moves:
                return "A"
            if [i + 1, j - 1] in a_moves and [i + 2, j - 2] in a_moves:
                return "A"

        for i, j in b_moves:
            if [i + 1, j] in b_moves and [i + 2, j] in b_moves:
                return "B"
            if [i, j + 1] in b_moves and [i, j + 2] in b_moves:
                return "B"
            if [i + 1, j + 1] in b_moves and [i + 2, j + 2] in b_moves:
                return "B"
            if [i + 1, j - 1] in b_moves and [i + 2, j - 2] in b_moves:
                return "B"

        if len(moves) < 9:
            return "Pending"

        return "Draw"


