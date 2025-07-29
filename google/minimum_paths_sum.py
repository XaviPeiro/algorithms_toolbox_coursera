from typing import List, Optional


class Solution:

    def get_left_cell_v(self, grid: List[List[int]], row: int, col: int) -> Optional[int]:
        if col > 0:
            return grid[row][col - 1]
        else:
            return None

    def get_top_cell_v(self, grid: List[List[int]], row: int, col: int) -> Optional[int]:
        if row > 0:
            return grid[row - 1][col]
        else:
            return None

    def minPathSum(self, grid: List[List[int]]) -> int:
        for krow, row in enumerate(grid):
            for kcol, col in enumerate(row):
                # get left and top cell
                if krow + kcol == 0:
                    continue

                left = self.get_left_cell_v(grid=grid, row=krow, col=kcol)
                top = self.get_top_cell_v(grid=grid, row=krow, col=kcol)
                # get min(left, top)
                if not isinstance(left, int):
                    left = float("inf")
                if not isinstance(top, int):
                    top = float("inf")
                min_value = min(left, top)

                # add(min_value, curr_value)
                grid[krow][kcol] += min_value
        return grid[-1][-1]




"""
    Alg analysis:
         !(n-1)
"""

if __name__ == '__main__':
    s = Solution()

    assert s.minPathSum(grid=[[1,3,1],[1,5,1],[4,2,1]]) == 7
