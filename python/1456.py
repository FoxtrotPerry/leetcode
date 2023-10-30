# O(n)


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        substr_vowels, max_vowels = 0, 0
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(len(s)):
            char = s[i]
            if char in vowels:
                substr_vowels += 1
            if i >= k and s[i - k] in vowels:
                substr_vowels -= 1
            max_vowels = max(max_vowels, substr_vowels)
        return max_vowels


print(Solution.maxVowels(None, "abciiidef", 3))
