class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr, max_length = 0, 0, 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                max_length = max(max_length, curr + prev)
                prev = curr
                curr = 0
        max_length = max(max_length, curr + prev)
        return max_length - 1 if max_length == len(nums) else max_length


# print(Solution.longestSubarray(None, [1, 1, 0, 1]))
# print(Solution.longestSubarray(None, [0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(Solution.longestSubarray(None, [1, 1, 0, 0, 1, 1, 1, 0, 1]))
