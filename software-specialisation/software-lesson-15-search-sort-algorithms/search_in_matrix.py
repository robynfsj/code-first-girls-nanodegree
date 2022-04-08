"""Software week 4 homework - search in matrix

You are given a matrix (a list of lists) of DISTINCT integers and a target
number. Each row in the matrix is SORTED and each column in the matrix is
SORTED. Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the
target integer IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
    [ 1,   4,   7,  12,  15, 1000],
    [ 2,   5,  19,  31,  32, 1001],
    [ 3,   8,  24,  33,  35, 1002],
    [40,  41,  42,  44,  45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 44

EXAMPLE OUTPUT

result = [3, 3]  - Not the best example output we could have been given!!
                   Which one is row and which one is column? Should have picked
                   a different target number as the example.
"""

example_matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

example_target = 99


# —————————————————————————————————————————————————————————————————————————————
# MOST EFFICIENT
# —————————————————————————————————————————————————————————————————————————————

def search_in_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return [-1, -1]


# —————————————————————————————————————————————————————————————————————————————
# WORKINGS OUT
# —————————————————————————————————————————————————————————————————————————————

# 1. Iterate over each number in each list until it finds the target.
# -------------------------------------------------------------------
# time O(n^2) - for loop inside another for loop
# space O(1) - there are only ever two int values stored (row_idx and col_idx)
#              regardless of size of inputs (although with a very big matrix
#              with lots of rows or cols, the values of the ints could get very
#              big and I'm guessing an extremely large int would take up more
#              memory than a smaller one?)

def search_in_matrix1(matrix, target):
    row_idx = -1

    for lst in matrix:
        row_idx += 1
        col_idx = -1

        for num in lst:
            col_idx += 1

            if num == target:
                return [row_idx, col_idx]

    return [-1, -1]


# print(search_in_matrix1(example_matrix, example_target))


# 2. Using enumerate function
# ---------------------------
# Probably better than solution 1 as it doesn't store counts in variables.
# But I'm not sure of the inner workings of enumerate so maybe that is doing
# something similar within it. It looks neater and is easier to follow at least.

# time O(n^2) - for loop inside another for loop
# space O(1) - no values are stored?

def search_in_matrix2(matrix, target):
    for row_idx, lst in enumerate(matrix):
        for col_idx, num in enumerate(lst):
            if num == target:
                return [row_idx, col_idx]
    return [-1, -1]


# print(search_in_matrix2(example_matrix, example_target))


# 3. Take advantage of matrix being sorted
# ----------------------------------------
# It says the values in rows and columns are sorted. This means we can probably
# skip some values and save iteration time, although it won't change the Big O
# notation because it will still include a for loop within a for loop. And for
# the particular matrix provided as an example, it won't reduce the number of
# iterations very much as the last column has such high numbers.

def search_in_matrix3(matrix, target):
    if matrix[0][0] <= target <= matrix[-1][-1]:
        for row_idx, lst in enumerate(matrix):
            if lst[0] <= target <= lst[-1]:
                for col_idx, num in enumerate(lst):
                    if num == target:
                        return [row_idx, col_idx]
    return [-1, -1]


# print(search_in_matrix3(example_matrix, example_target))


# 4. Start eliminating elsewhere
# ------------------------------
# I did not come up with this answer myself, but understand that it is the most
# efficient. I have commented on the function extensively to demonstrate my
# understanding and for my own future reference.
#
# I was on the right track with my third approach by eliminating rows from my
# search. However, I did not start the eliminations in the optimum place. Where
# as my previous approach only worked by eliminating rows from consideration,
# this approach is able to eliminate both rows and columns from consideration
# by starting the search in the top right of the matrix. If the target is
# greater than this value, we can eliminate that row. If the target is smaller
# than that this value, we can eliminate that column.


def search_in_matrix4(matrix, target):
    # Set index of top right value in matrix.
    row = 0
    col = len(matrix[0]) - 1  # length of row (minus 1 to account for index 0)

    # Loop over rows and columns depending on the value at the position in the
    # matrix that we are up to.
    while row < len(matrix) and col >= 0:

        # If the value matches the target, return the row and column indexes.
        if matrix[row][col] == target:
            return [row, col]

        # If the value is greater than the target, eliminate the column from
        # consideration and move our search to the column to the left.
        if matrix[row][col] > target:
            col -= 1

        # Else (i.e. if the value is less than the target), eliminate the row
        # from consideration and move our search to the next row.
        else:
            row += 1

    return [-1, -1]

# print(search_in_matrix4(example_matrix, example_target))
