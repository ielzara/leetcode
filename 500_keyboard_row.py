from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letters1 = "qwertyuiop"
        letters2 = "asdfghjkl"
        letters3 = "zxcvbnm"
        new_word = ""
        new_list =[]
        for word in words:
            for letter in word:
                if letter in letters1:
                    new_word += letter
            if new_word == word:
                new_list.append(new_word)
        return new_list


