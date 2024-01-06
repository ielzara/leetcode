from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        numWords = len(words)

        for i in range(numWords):
            for j in range(len(words[i])):
                if j >= numWords or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False

        return True
