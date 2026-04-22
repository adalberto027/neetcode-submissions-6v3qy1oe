# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = 0

        def dfs(r: Optional[TreeNode], target: int) -> int:
            if not r:
                return 0

            l =  dfs(r.left, target)
            print(r.val)
            self.count += 1
            if self.count == target:
                self.ans = r.val
            ri = dfs(r.right, target)

            return l + ri

        dfs(root, k)
        return self.ans