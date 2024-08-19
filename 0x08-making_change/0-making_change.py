#!/usr/bin/python3
"""Define modeule"""


def makeChange(coins, total):
    """Make change"""

    if total <= 0:
        return 0

    steps_num, sum = 0, 0

    coins.sort(reverse=True)

    for coin in coins:
        while sum + coin <= total:
            steps_num += 1
            sum += coin

        if sum == total:
            return steps_num

    return -1
