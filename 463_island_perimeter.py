class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # Check Up
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1

                    # Check Down
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        perimeter += 1

                    # Check Left
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1

                    # Check Right
                    if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter


#         for each row in the grid:
#             for each cell in the row:
#                 if the cell is land (1):
#                    check each of the four adjacent sides (up, down, left, right)
#                     for each side:
#                         if the side is either at the edge of the grid or adjacent to water (0):
#                             increment the perimeter by 1
# return perimeter
