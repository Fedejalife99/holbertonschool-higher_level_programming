#!/usr/bin/python3
"""define a pascal triangle function"""


def pascal_triangle(n):
    """returns the triangle"""
    if n <= 0:
        return []

    row_1 = [1]
    triangle = [row_1]
    for i in range(1, n):
        p_row = row_1
        row_1 = [1]
        for j in range(1, i):
            row_1.append(p_row[j-1] + p_row[j])
        row_1.append(1)
        triangle.append(row_1)

    return triangle
