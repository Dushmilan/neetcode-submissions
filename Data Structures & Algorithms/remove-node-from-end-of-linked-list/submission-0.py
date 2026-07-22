# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def find_len(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        node_to_remove = find_len(head)-n

        if node_to_remove == 0:
            return head.next
        
        curr = head
        track=0
        while curr:
            if track == node_to_remove-1:
                curr.next = curr.next.next
                break
            track+=1
            curr = curr.next
            
        return head