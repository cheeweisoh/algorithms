from fractions import gcd

from structures import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        def helper(currNode, nextNode):
            if nextNode is None:
                return
            else:
                insertNode = ListNode(gcd(currNode.val, nextNode.val), nextNode)
                currNode.next = insertNode
                helper(nextNode, nextNode.next)

        helper(head, head.next)
        return head
