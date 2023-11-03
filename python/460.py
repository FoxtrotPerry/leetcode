from typing import Optional

# NOT COMPLETE. Passes 73/92 testcases


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if not root.left and not root.right:
            if key == root.val:
                root = None
            return root

        def rec_traverse(tn):
            if not tn:
                return tn
            # if found, no recursion
            if tn.val == key:
                if tn.right:
                    tn.val, tn.right = tn.right.val, tn.right.right
                elif tn.left:
                    tn.val, tn.left = tn.left.val, tn.left.right
                else:
                    return "found"
            else:
                # if not found, keep searching each branch
                if tn.left:
                    left = rec_traverse(tn.left)
                    if left == "found":
                        tn.left = None
                if tn.right:
                    right = rec_traverse(tn.right)
                    if right == "found":
                        tn.right = None

        rec_traverse(root)
        print(root)
        return root
