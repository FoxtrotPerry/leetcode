# loop will:
# 1. find the first char
# 2. save location of first char
# 3. continue incrementing until space or end of string is found
# 4. save location of first space
# 5. save substring of first char location and first space location to word
#    array

# end loop when the location on step 3 is -1


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split_list = s.split(" ")
        reverse_word_string = ""
        # for every potential word in the reversed split_list
        for potential_word in split_list[::-1]:
            # if the contents aren't empty (therefore a word)
            if potential_word != "":
                # tack it onto the end of out reverse_word_string
                reverse_word_string += potential_word + " "
        # strip the last char since the last added space isn't needed
        return reverse_word_string.strip()


# First attempt (didn't know a few things about python so I reinvented the
# wheel in a few places)


# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s_list = list(s.strip())
#         end_of_list_pos = len(s_list) - 1
#         index = 0
#         word_array = []
#         # start of loop described above
#         while index < len(s_list):
#             # step 1
#             start_of_word_pos = -1
#             while start_of_word_pos == -1:
#                 if s_list[index].isalnum():
#                     start_of_word_pos = index
#                     continue
#                 index += 1
#             # index should be one ahead of the found char's position
#             end_of_word_pos = -1
#             # while the next space isn't known
#             while end_of_word_pos == -1 and end_of_word_pos != len(s_list):
#                 print(index, end_of_list_pos)
#                 if s_list[index] == " ":
#                     end_of_word_pos = index
#                 elif index >= end_of_list_pos:
#                     end_of_word_pos = len(s_list)
#                 index += 1
#             new_word = "".join(s_list[start_of_word_pos:end_of_word_pos])
#             word_array.append(new_word)
#         word_array.reverse()
#         return " ".join(word_array)


print(Solution.reverseWords(None, "blue is sky the"))
print(Solution.reverseWords(None, "  hello world  "))
print(Solution.reverseWords(None, "a good   example"))
print(Solution.reverseWords(None, "F R  I   E    N     D      S      "))
print(Solution.reverseWords(None, " asdasd df f"))
