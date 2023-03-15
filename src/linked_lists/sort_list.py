from src.models.list_node import ListNode


class SortList(object):
    def sort(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Find the middle of the list
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        prev.next = None

        # Recursively sort each half
        left = self.sort(head)
        right = self.sort(slow)

        # Merge the two sorted halves
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next
