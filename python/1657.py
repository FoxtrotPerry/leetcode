from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        letter_count1, letter_count2 = Counter(word1), Counter(word2)
        if letter_count1 == letter_count2:
            return True
        num_count1 = Counter([count for count in letter_count1.values()])
        num_count2 = Counter([count for count in letter_count2.values()])
        return num_count1 == num_count2 and set(word1) == set(word2)


print(Solution.closeStrings(None, "cabbba", "abbccc"))
