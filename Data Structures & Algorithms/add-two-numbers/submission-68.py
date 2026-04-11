# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:

            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        ans = None
        p = ans   
        next_ = 0

        lefts = 0
        while l1 or l2:
            if l1 and l2:
                if not ans:
                    ans = ListNode(0)
                    p = ans
                else:
                    ans.next = ListNode(0)
                    ans = ans.next
                print(0)
                temp = l1.val + l2.val + lefts      
                ans.val = temp % 10 
                lefts = int(temp/10)
                l1 = l1.next
                l2 = l2.next
                
            elif not l1:
                print(2)
                while l2:
                    print(2)
                    temp = l2.val + lefts
                    ans.next = ListNode(temp % 10)
                    ans = ans.next
                    lefts = int(temp/10)
                    l2 = l2.next
                if lefts > 0:
                    ans.next = ListNode(lefts)
                return p

            elif not l2:
                while l1:
                    print(3)
                    temp = l1.val + lefts
                    ans.next = ListNode(temp % 10)
                    ans = ans.next
                    lefts = int(temp/10)
                    l1 = l1.next
                if lefts > 0:
                    ans.next = ListNode(lefts)

                return p
            
        if lefts > 0:
            ans.next = ListNode(lefts)
        return p
            

