# Approach:
# 1 find the first [
# 2 if not found, return the string as is
# 3 if found, look for a '[' and a ']' at the same time
# 4 if the ']' is found before another '[', then there's no nesting
# 5 if the '[' is found before the ']', there's nesting that needs to be accounted for
# 6 if nesting is found, start from the newly found '[' and look for it's closing tag
# 7 repeat 3 through 6 until closing pairs are found with no nesting in between


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                res = ""
                while stack[-1] != "[":
                    res += stack.pop()
                stack.pop()
                num_str = ""
                while len(stack) != 0 and stack[-1].isdigit() is True:
                    num_str += stack.pop()

                stack.append(res * int(num_str[::-1]))
        return "".join([word[::-1] for word in stack])


print(Solution.decodeString(Solution, "3[a]2[bc]"))
print(Solution.decodeString(Solution, "3[a2[c]]"))
print(Solution.decodeString(Solution, "2[abc]3[cd]ef"))
