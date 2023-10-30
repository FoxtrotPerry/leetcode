class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero_cnt, l = 0, 0
        # for every index and number in the num list
        for i, num in enumerate(nums):
            # if the num == 0
            if num == 0:
                # increment zero count
                zero_cnt += 1
            # if the zero count if now more than the # allowed
            if zero_cnt > k:
                # decrement the zero_cnt if the series_start
                # is a zero
                zero_cnt -= 1 if nums[l] == 0 else 0
                # and increment the series_start so we can move
                # on to the next series possibility
                l += 1
        # return the length of the initial list, minus the series_start
        return len(nums) - l


# print(Solution.longestOnes(None, [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.longestOnes(None, [0, 0, 1, 1, 1, 0, 0], 0))
# print(
#     Solution.longestOnes(
#         None, [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
#     )
# )
