# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(r: Optional[TreeNode], target: int) -> int:
            if not r:
                return []
            return dfs(r.left, target) + [r.val] + dfs(r.right, target)
        return dfs(root, k) [k-1]