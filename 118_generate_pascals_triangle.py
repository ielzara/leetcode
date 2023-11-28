from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(ret[i - 1][j - 1] + ret[i - 1][j])
            row.append(1)
            ret.append(row)
        return ret

x = Solution()
print(x.generate(5))
