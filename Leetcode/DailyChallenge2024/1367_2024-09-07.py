from typing import Optional

from structures import ListNode, TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            if not head:
                return True
            if not root or head.val != root.val:
                return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        if not root:
            return False
        return (
            dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )
