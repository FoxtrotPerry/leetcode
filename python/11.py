# O(n) solution


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            area = min([height[left], height[right]]) * (right - left)
            if area > max_area:
                max_area = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


print(Solution.maxArea(None, [1, 8, 6, 2, 5, 4, 8, 3, 7]))


# O(n^2) solution:

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 area = (j - i) * min([height[j], height[i]])
#                 if area > max_area:
#                     max_area = area
#         return max_area
