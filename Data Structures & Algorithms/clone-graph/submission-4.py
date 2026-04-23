"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        graph = defaultdict(list)
        def dfs(node: Optional['Node']):
            for e in node.neighbors:
                graph[node.val].append(e.val)
                if e.val not in graph:
                    dfs(e)
        dfs(node)
        if not graph:
            return Node(node.val)
        mappingKeys = {e: Node(e) for e in graph}

        ans = None
        for e in graph:
            if mappingKeys[e].val == node.val:
                ans = mappingKeys[e]
            for n in graph[e]:
                mappingKeys[e].neighbors.append(mappingKeys[n])
        seen = set()
        return ans
        