# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return (lambda f:f(root,root.val,root.val,f))(lambda n,a,b,f:n!=None and max(abs(n.val-a),abs(n.val-b),f(n.left,min(n.val,a),max(n.val,b),f),f(n.right,min(n.val,a),max(n.val,b),f)))
