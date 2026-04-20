# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root) -> list[int]:
            if not root:
                return [None]
            return dfs(root.left) + [root.val] + dfs(root.right)
        self.t = dfs(subRoot)
        def dfsModified(root) -> list[int]:
            if not root:
                return False
            if dfs(root) == self.t:
                return True
            return dfsModified(root.left) or dfsModified(root.right)
        return dfsModified(root)
        

