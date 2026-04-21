from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = [root.val]
        stack = deque([root])

        while stack:
            temp = deque([])
            for n in stack:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            if temp:
                ans.append(temp[-1].val)
            stack = temp
        return ans
        