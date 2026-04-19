# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def r(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return max(r(root.left) + 1, r(root.right) + 1)
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right), (r(root.left) + r(root.right)))
        return dfs(root)
        