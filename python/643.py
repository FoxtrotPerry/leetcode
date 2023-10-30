# O(n)


class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        for i in range(len(nums) - k):
            curr_sum = curr_sum + nums[i + k] - nums[i]
            max_sum = max(max_sum, curr_sum)
        return float(max_sum) / float(k)


# Doesn't pass all submission tests:

# from sys import maxsize


# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
#         max_sum = -maxsize
#         hm = {}
#         for i in range(len(nums)):
#             # assign the value to it's spot in the hash map
#             hm[i % k] = nums[i]
#             curr_values = hm.values()
#             if len(curr_values) == k:
#                 if len(curr_values) + 1 == k:
#                     replaced_val = nums[i - k]
#                     if hm[i % k] < replaced_val:
#                         continue
#                 new_sum = sum(curr_values)
#                 if new_sum > max_sum:
#                     max_sum = new_sum
#         return float(max_sum) / float(k)
