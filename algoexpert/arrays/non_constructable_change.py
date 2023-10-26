"""https://www.algoexpert.io/questions/non-constructible-change"""


def nonConstructibleChange(coins):
    if not coins:
        return 1

    coins.sort()
    m = 0
    for c in coins:
        if c > m + 1:
            break
        m += c
    return m+1