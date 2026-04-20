# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maxValue: int) -> int:
            if not root:
                return 0
            if root.val >= maxValue:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            return dfs(root.left, maxValue) + dfs(root.right, maxValue)
        return dfs(root, float('-inf'))        