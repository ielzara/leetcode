from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        max_candy = len(candyType)//2

        variety = len(set(candyType))

        if max_candy <= variety:
            return max_candy
        else:
            return variety