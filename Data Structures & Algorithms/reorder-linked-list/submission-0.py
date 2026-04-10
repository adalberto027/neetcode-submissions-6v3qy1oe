# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev

        if not head.next:
            return
        
        slow, fast = head, head
        p1 = slow

        while fast.next.next and fast.next.next.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = reverse(slow.next)
        firstHalf = slow
        firstHalf.next = None
        firstHalf = p1

        while firstHalf:
            temp1 = firstHalf
            firstHalf = firstHalf.next
            temp1.next = None
            
            temp2 = secondHalf
            secondHalf = secondHalf.next
            temp2.next = None

            temp1.next = temp2
            temp2.next =firstHalf

            if not firstHalf and secondHalf:
                temp2.next = secondHalf