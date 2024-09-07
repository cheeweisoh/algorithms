# import collections
# import math
# import random
# import heapq

# import string
# import bisect
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
        return dfs(head, root) or dfs(head, root.left) or dfs(head, root.right)


def main():
    soln = Solution()
    chalk = [3, 4, 1, 2]
    k = 25
    print(soln.chalkReplacer(chalk, k))


if __name__ == "__main__":
    main()
