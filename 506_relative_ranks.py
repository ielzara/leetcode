from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def assignScores(self, score: List[int]):
            new_list = sorted(score, reverse=True)
            score_list = {}
            for i, number in enumerate(new_list):
                if i == 0:
                    score_list[number] = "Gold Medal"
                elif i == 1:
                    score_list[number] = "Silver Medal"
                elif i == 2:
                    score_list[number] = "Bronze Medal"
                else:
                    score_list[number] = str(i + 1)
            return score_list

        scores_dict = assignScores(self, score)
        answer = []
        for number in score:
            answer.append(scores_dict.get(number))
        return answer
