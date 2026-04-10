# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head.next, head

        while fast and slow:

            

            if slow == fast:
                return True

            if slow and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False

        return False
        