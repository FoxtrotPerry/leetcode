class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        i = 0
        while True:
            if i == len(chars):
                break
            # instantiate group counter
            num_in_group = 0
            # get next char
            char = chars[i]
            while i != len(chars) and chars[i] == char:
                num_in_group += 1
                chars.pop(i)
            s += char
            if num_in_group >= 2:
                s += str(num_in_group)
        chars += list(s)
        return len(chars)


input_list = ["a", "a", "b", "b", "c", "c", "c"]
print(Solution.compress(None, input_list))
print(input_list)
