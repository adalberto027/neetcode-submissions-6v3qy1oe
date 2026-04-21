from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque([root])
        while stack and stack[0]:
            temp = deque([])
            ans.append(stack[-1].val)
            for n in stack:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            stack = temp
        return ans
        