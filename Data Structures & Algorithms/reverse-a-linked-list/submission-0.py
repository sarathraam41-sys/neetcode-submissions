class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        current = head
        while current:
            current.val = stack.pop()
            current = current.next
        return head
