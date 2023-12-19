from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = len(wordsDict)
        index2 = len(wordsDict)
        min_distance = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1 or word == word2:
                if word == word1:
                    index1 = i
                else:
                    index2 = i
                if index1 != len(wordsDict) and index2 != len(wordsDict):
                    min_distance = min(min_distance, abs(index1 - index2))
        return min_distance
