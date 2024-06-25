# import collections
# import math

# import random
# import heapq

# import string
# import bisect
from structures import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val = 0

        def dfs(node):
            global val
            if not node:
                return

            dfs(node.right)
            val += node.val
            node.val = val
            dfs(node.left)

        dfs(root)
        return root


def main():
    soln = Solution()


if __name__ == "__main__":
    main()
