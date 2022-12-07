# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return root and(root.val>=low and self.rangeSumBST(root.left,low,high))+(root.val<=high and self.rangeSumBST(root.right,low,high)+(low<=root.val<= high and root.val))or 0
