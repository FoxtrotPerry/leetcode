from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root is not None:
                root.right, root.left = root.left, root.right
                if root.left is not None:
                    invert(root.left)
                if root.right is not None:
                    invert(root.right)

        print(root)
        invert(root)
        return root
