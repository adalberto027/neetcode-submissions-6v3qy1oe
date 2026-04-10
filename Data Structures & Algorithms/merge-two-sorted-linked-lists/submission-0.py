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
        r = None
        ans = None
        curList1 = list1
        curList2 = list2

        while curList1 or curList2:

            if not ans:
                if curList1.val < curList2.val:
                    ans = curList1
                    r = ans
                    curList1 = curList1.next
                else:
                    ans = curList2
                    r = ans
                    curList2 = curList2.next
            else:

                if not curList1:
                    ans.next = curList2
                    break
                if not curList2:
                    ans.next = curList1
                    break

                if curList1.val < curList2.val:
                    print(curList1.val)
                    ans.next = curList1
                    curList1 = curList1.next
                else:
                    print(curList2.val)
                    ans.next = curList2
                    curList2 = curList2.next
                ans = ans.next
        return r
                

        