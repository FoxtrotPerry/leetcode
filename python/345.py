class Solution:
    def reverseVowels(self, s: str) -> str:
        # instantiate a list of vowels
        vowels = ["a", "e", "i", "o", "u"]
        # convert the string into a list of chars
        s = list(s)
        # instantiate two pointers, one will go forward through the char array, the
        # other will go backwards
        forward_index = 0
        reverse_index = len(s) - 1
        # while the two pointers haven't passed each other
        while forward_index < reverse_index:
            # check if the char at the forward pointer is a vowel
            if s[forward_index].lower() not in vowels:
                # if not, increment the forward pointer without swapping vowels
                forward_index += 1
            elif s[reverse_index].lower() not in vowels:
                # same thing for the reverse pointer but we decrement the
                # reverse pointer
                reverse_index -= 1
            else:
                # if both pointers are at vowels, swap them and advance both
                # pointers in their respective directions
                s[forward_index], s[reverse_index] = s[reverse_index], s[forward_index]
                forward_index += 1
                reverse_index -= 1
        return "".join(s)


print(Solution.reverseVowels(None, "hello"))
print(Solution.reverseVowels(None, "leetcode"))
