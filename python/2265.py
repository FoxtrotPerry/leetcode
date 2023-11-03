from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        avg_match = 0

        def rec_traverse(tn):
            # allow the count to be accessed from outside the func's scope
            nonlocal avg_match

            if not tn:
                return 0, 0

            left_sum, left_cnt = rec_traverse(tn.left)
            right_sum, right_cnt = rec_traverse(tn.right)

            curr_node_sum = tn.val + left_sum + right_sum
            curr_node_cnt = 1 + left_cnt + right_cnt

            if curr_node_sum // curr_node_cnt == tn.val:
                avg_match += 1

            return curr_node_sum, curr_node_cnt

        rec_traverse(root)

        return avg_match
