class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = self.findLength(head)
        i, traverseTill = 0, length - n - 1
        if traverseTill == -1:
            return head.next
        curr = head
        while i < traverseTill:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head

    def findLength(self, head):
        count = 0
        if head is None:
            return count
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return count