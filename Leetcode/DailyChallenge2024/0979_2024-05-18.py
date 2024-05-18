class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1

        self.moves = 0
        dfs(root)
        return self.moves
