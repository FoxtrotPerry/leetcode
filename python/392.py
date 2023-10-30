class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)

        search_pos = 0

        for letter in s_list:
            if letter in t_list[search_pos:]:
                search_pos = t_list.index(letter, search_pos) + 1
            else:
                return False
        return True


print(Solution.isSubsequence(None, "abc", "ahbgdc"))
print(Solution.isSubsequence(None, "axc", "ahbgdc"))
