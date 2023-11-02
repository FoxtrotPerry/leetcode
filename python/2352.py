from typing import List


# Doesn't work. Still working on it...


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mirror_cells = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == grid[j][i]:
                    print(True)
                    mirror_cells += 1
                else:
                    print(False)
        if len(grid) > 2:
            return mirror_cells // len(grid)
        else:
            return mirror_cells


print(Solution.equalPairs(None, [[11, 1], [1, 11]]))
