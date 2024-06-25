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
