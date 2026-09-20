class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the list
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        prev, curr = None, second

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 4: Merge the two halves
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2