from sys import maxsize


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest_num = maxsize
        second_smallest_num = maxsize

        for num in nums:
            if smallest_num >= num:
                smallest_num = num
            elif second_smallest_num >= num:
                second_smallest_num = num
            else:
                return True
        return False


print(Solution.increasingTriplet(None, [1, 2, 3, 4, 5]))
print(Solution.increasingTriplet(None, [5, 4, 3, 2, 1]))
print(Solution.increasingTriplet(None, [2, 1, 5, 0, 4, 6]))
