#!/usr/bin/python3
"""Define module"""


def makeChange(coin_denominations, amount):
    """Make change"""

    if amount <= 0:
        return 0

    num_coins_used, current_sum = 0, 0

    coin_denominations.sort(reverse=True)

    for coin in coin_denominations:
        while current_sum + coin <= amount:
            num_coins_used += 1
            current_sum += coin

        if current_sum == amount:
            return num_coins_used

    return -1
