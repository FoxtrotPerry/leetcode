# loop will:
# 1. find the first char
# 2. save location of first char
# 3. continue incrementing until space or end of string is found
# 4. save location of first space
# 5. save substring of first char location and first space location to word array

# end loop when the location on step 3 is -1


class Solution:
    def reverseWords(self, s: str) -> str:
        index = 0
        word_array = []
        while index != -1:
            index = s.find(" ", index)
            end_of_word = s.find(" ", index)


print(Solution.reverseWords(None, "blue is sky the"))
print(Solution.reverseWords(None, "  hello world  "))
print(Solution.reverseWords(None, "a good   example"))
