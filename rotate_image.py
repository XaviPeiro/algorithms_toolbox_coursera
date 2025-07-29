from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def four_swaps(matrix, startp: tuple):
            irow, icol = startp
            prev = matrix[]
            nonlocal visited
            l = len(matrix) - 1
            for _ in range(4):
                tmp = matrix[irow][icol]
                visited.append((irow, icol))
                if prev is not None:
                    matrix[irow][icol] = prev
                prev = tmp
                irow, icol = icol, l - irow

        visited = []
        for irow, row in enumerate(matrix):
            for icol, col in enumerate(matrix):
                if (irow, icol) in visited:
                    continue
                four_swaps(matrix, (irow, icol))


if __name__ == "__main__":
    s = Solution()
    assert s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7,4,1],[8,5,2],[9,6,3]]

