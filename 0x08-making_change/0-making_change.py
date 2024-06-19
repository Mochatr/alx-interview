#!/usr/bin/python3
"""
Module to solve the coin change problem.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.

    Param:
        coins[list]: List of values of the coins in your possession
        total[int]: Total amount to meet

    Return:
        Fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] != float('inf'):
        return dp[total]

    else:
        return -1
