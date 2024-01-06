from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        count = 0

        g.sort()
        s.sort()

        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
               i += 1
               j += 1
               count +=1
            else:
               j += 1
        return count