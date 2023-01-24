#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if (n < 1):
        return []
    if (n == 1):
        return [[1]]

    triangle = [[1]]

    for i in range(1, n):
        prevRow = triangle[i-1]
        currRow = []

        currRow.append(1)

        for j in range(1, len(prevRow)):
            currRow.append(prevRow[j] + prevRow[j-1])

        currRow.append(1)

        triangle.append(currRow)

    return triangle
