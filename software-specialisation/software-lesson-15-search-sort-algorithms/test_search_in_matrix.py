from unittest import TestCase, main
from search_in_matrix import search_in_matrix


class TestSearchInMatrix(TestCase):

    example_matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]

    def test_num_found(self):
        matrix = TestSearchInMatrix.example_matrix

        target1 = 44  # example case provided in homework
        output1 = search_in_matrix(matrix, target1)
        expected1 = [3, 3]
        self.assertEqual(output1, expected1)

        target2 = 1000  # target in first list and last in list
        output2 = search_in_matrix(matrix, target2)
        expected2 = [0, 5]
        self.assertEqual(output2, expected2)

        target3 = 99  # target in last list and first in list
        output3 = search_in_matrix(matrix, target3)
        expected3 = [4, 0]
        self.assertEqual(output3, expected3)

    def test_num_not_found(self):
        matrix = TestSearchInMatrix.example_matrix
        expected = [-1, -1]

        target1 = 46  # within range of numbs in matrix
        output1 = search_in_matrix(matrix, target1)
        self.assertEqual(output1, expected)

        target2 = 2039525  # outside range of numbs in matrix
        output2 = search_in_matrix(matrix, target2)
        self.assertEqual(output2, expected)


if __name__ == '__main__':
    main()
