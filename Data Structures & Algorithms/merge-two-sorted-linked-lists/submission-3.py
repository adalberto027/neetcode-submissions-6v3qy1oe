# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2
        ans = None
        r = ans

        while cur1 or cur2:
            if not ans:
                if cur1.val <= cur2.val:
                    temp = cur1
                    cur1 = cur1.next
                    ans = temp
                    r = ans
                else:
                    temp = cur2
                    cur2 = cur2.next
                    ans = temp
                    r = ans
            elif cur1 and cur2:
                if cur1.val <= cur2.val:
                    temp = cur1
                    cur1 = cur1.next
                    ans.next = temp
                    ans = ans.next
                else:
                    temp = cur2
                    cur2 = cur2.next
                    ans.next = temp
                    ans = ans.next
            elif not cur1 and not cur2:
                break
            elif cur1:
                ans.next = cur1
                return r
            else: 
                ans.next = cur2
                return r
        return r


        