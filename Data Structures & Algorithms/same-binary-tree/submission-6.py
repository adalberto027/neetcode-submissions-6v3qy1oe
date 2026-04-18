# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(root: Optional[TreeNode]):
            if not root:
                return [None]
            return inOrder(root.right) + inOrder(root.left) + [root.val]
    
        return inOrder(p) == inOrder(q)