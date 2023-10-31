from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_seq, root2_seq = [], []

        def search(root, rootVal, seq):
            if not root.left and not root.right:
                seq.append(root.val)
            else:
                if root.left:
                    search(root.left, root.val, seq)
                if root.right:
                    search(root.right, root.val, seq)

        search(root1, root1.val, root1_seq)
        search(root2, root2.val, root2_seq)

        print(root1_seq)
        print(root2_seq)

        return root1_seq == root2_seq
