#!/usr/bin/python3
"""Island perimeter problem"""


def island_perimeter(grid):
    """gets perimeter"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
