from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        stack = deque([root])
        nextLevel = deque([])
        temp = []
        while stack:
            cur = stack.popleft()
            if cur.left:
                temp.append(cur.left.val)
                nextLevel.append(cur.left)
            if cur.right:
                temp.append(cur.right.val)
                nextLevel.append(cur.right)
            if not stack and nextLevel:
                stack = nextLevel
                ans.append(temp)
                temp = []
                nextLevel = deque([])
        return ans       