# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        if fast and fast.next:
            fast = fast.next.next
        else:
            return False

        while slow:
            if slow == fast:
                return True
            else:
                if fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    return False
        return False
        