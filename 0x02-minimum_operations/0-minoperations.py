#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the fewest number
    of the operations to get exactly n 'H'
    characters in the file.

    Args:
      n (int): Target number of 'H' characters to achieve.

    Returns:
      int: Minimum number of operations required, or 0
      if n is impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
