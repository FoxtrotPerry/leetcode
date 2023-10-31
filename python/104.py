from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                # when we've reached the end of the branch, return the depth
                return depth
            # recursively call dfs and select the node with the highest value
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        # start the recursion by calling dfs with the root arg
        return dfs(root, 0)
