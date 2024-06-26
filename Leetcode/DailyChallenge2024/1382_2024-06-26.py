from structures import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            nonlocal nodes

            if not node:
                return

            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        def bs(s, e):
            nonlocal nodes
            if s > e:
                return

            mid = (s + e) // 2
            root = nodes[mid]
            root.left = bs(s, mid - 1)
            root.right = bs(mid + 1, e)

            return root

        dfs(root)
        return bs(0, len(nodes) - 1)
