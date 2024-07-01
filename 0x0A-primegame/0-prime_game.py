#!/usr/bin/python3
"""Define function"""


def sieve_of_eratosthenes(n):
    """
    Use Sieve of Eratosthenes to generate
    a list of primes up to n
    """
    is_prime = [True] * (n + 1)
    p = 2

    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def count_wins(n):
    """
    Count how many times each player wins with n numbers.
    """
    primes = sieve_of_eratosthenes(n)
    win_count = [0] * (n + 1)

    for i in range(1, n + 1):
        if win_count[i] == 0:
            win_count[i] = 1
            for prime in primes:
                if prime * i > n:
                    break
                win_count[prime * i] = 2

    return win_count


def isWinner(x, nums):
    """
    Determine the winner after x rounds
    """
    if not nums or x <= 0:
        return None

    max_num = max(nums)
    win_count = count_wins(max_num)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if win_count[num] == 1:
            maria_wins += 1
        elif win_count[num] == 2:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
