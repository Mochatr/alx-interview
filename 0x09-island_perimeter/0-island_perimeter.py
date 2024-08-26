#!/usr/bin/python3
"""Define Function"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    for i, row in enumerate(grid):
        for j, is_land in enumerate(row):
            if is_land:
                perimeter += 4

                if (j + 1) < width and grid[i][j + 1]:
                    perimeter -= 1

                if (j - 1) >= 0 and grid[i][j - 1]:
                    perimeter -= 1

                if (j + 1) < height and grid[i + 1][j]:
                    perimeter -= 1

                if (j - 1) >= 0 and grid[i - 1][j]:
                    perimeter -= 1

    return perimeter
