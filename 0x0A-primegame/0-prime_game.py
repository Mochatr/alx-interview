#!/usr/bin/python3
"""Define functions."""


def isWinner(x, nums):
    """Determine the winner from prime game"""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    ben_score, maria_score = 0, 0

    for i in range(x):
        primes_count = sum(1 for prime in primes if prime <= nums[i])

        ben_score += primes_count % 2 == 0
        maria_score += primes_count % 2 == 1

    if ben_score == maria_score:
        return None

    return 'Ben' if ben_score > maria_score else 'Maria'


def sieve_of_eratosthenes(num):
    """
    Identify prime numbers up to max_n.
    """
    primes = [True] * (num + 1)
    primes[0], primes[1] = False, False

    p = 2

    while (p * p <= num):
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False

        p += 1

    return [i for i in range(num + 1) if primes[i]]
