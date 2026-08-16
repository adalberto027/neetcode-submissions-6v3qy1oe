# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        superslow = head
        slow = head
        fast = head
        times = n

        while fast and times:
            fast = fast.next
            times -= 1

        while fast:
            fast = fast.next
            if slow != superslow:
                superslow = superslow.next
            slow = slow.next
        if slow == superslow:
            return superslow.next
        else:
            superslow.next = slow.next
            return head 

        