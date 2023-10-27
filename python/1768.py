class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mstring: str = ""
        maxlen = len(word1) if len(word1) >= len(word2) else len(word2)
        for i in range(maxlen):
            if len(word1) > i:
                mstring += word1[i]
            if len(word2) > i:
                mstring += word2[i]
        return mstring
