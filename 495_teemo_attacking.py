from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timer= 0
        total = 0
        for i in range(0, len(timeSeries) - 1):
            if timeSeries[i] == timeSeries[i+1] +1:
                timer = 0
            timer += duration
            total = max(timer, total)
        return total

        