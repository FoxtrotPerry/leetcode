class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        move_count = 0
        for i in range(len(nums))[::-1]:
            if i + move_count == len(nums) and move_count > 0:
                break
            if nums[i + move_count] != 0:
                num_to_move = nums[i + move_count]
                del nums[i + move_count]
                nums.insert(0, num_to_move)
                move_count += 1


input_list = [0, 1, 0, 1]
# print(Solution.moveZeroes(None, [0, 0, 1]))
print(Solution.moveZeroes(None, input_list))
print(input_list)
