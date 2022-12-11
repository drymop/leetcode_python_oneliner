# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return (lambda f:f(root,f)[0])(lambda n,f:n and(lambda v,m1,p1,m2,p2:(max(m1,m2,max(p1,0)+v+max(p2,0)),v+max(p1,p2,0)))(n.val,*f(n.left,f),*f(n.right,f))or(-inf,-inf))
