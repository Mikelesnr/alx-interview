#!/usr/bin/python3
numRows = int(input("Enter number of rows: "))


def printPascal(numRows):
    if (numRows < 1):
        return []
    if (numRows == 1):
        return [[1]]

    triangle = [[1]]

    for i in range(1, numRows):
        prevRow = triangle[i-1]
        currRow = []

        currRow.append(1)

        for j in range(1, len(prevRow)):
            currRow.append(prevRow[j] + prevRow[j-1])

        currRow.append(1)

        triangle.append(currRow)

    print(triangle)


printPascal(numRows)
