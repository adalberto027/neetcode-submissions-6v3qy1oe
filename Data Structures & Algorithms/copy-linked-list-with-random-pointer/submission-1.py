"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        current2 = head
        nodes = {}
        randoms = {}
        originVals = {}

        ansHead = None
        p = None

        current = head
        counter = 0
        while current:
            if not ansHead:
                ansHead = Node(counter)
                p = ansHead
            else:
                ansHead.next = Node(counter)
                ansHead = ansHead.next
            originVals[counter] = current.val
            current.val = counter
            current = current.next
            nodes[counter] = ansHead
            counter += 1       
        
        current = head

        while current:
            if current.random:
                randoms[current.val] = current.random.val
            else:
                randoms[current.val] = current.random
            current = current.next
        
        current = p


        while current:
            if randoms[current.val] != None:
                current.random = nodes[randoms[current.val]]
            else:
                current.random = None
            current = current.next 

        current = p

        while current:
            current.val = originVals[current.val]
            current = current.next 
        
        return p
        