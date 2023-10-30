class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0
        hm = {}
        for num in nums:
            if k - num in hm and hm[k - num] > 0:
                pairs += 1
                hm[k - num] -= 1
            elif num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        return pairs


print(
    Solution.maxOperations(
        None, [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 6
    )
)
