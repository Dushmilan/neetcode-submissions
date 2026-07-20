# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptrA = list1
        ptrB = list2
        dummy = ListNode(0)
        tail = dummy
        while ptrA and ptrB:
            if ptrA.val>= ptrB.val:
                tail.next = ptrB
                ptrB = ptrB.next
            else:
                tail.next = ptrA
                ptrA = ptrA.next
            tail = tail.next
        tail.next = ptrA or ptrB
        return dummy.next
