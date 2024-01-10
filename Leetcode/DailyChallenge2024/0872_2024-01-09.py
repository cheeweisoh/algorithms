class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        lst1 = []
        lst2 = []

        def dfs(node, lst):
            if not node:
                return
            if not node.left and not node.right:
                lst.append(node.val)
                return
            if node.left:
                dfs(node.left, lst)
            if node.right:
                dfs(node.right, lst)

        dfs(root1, lst1)
        dfs(root2, lst2)

        return lst1 == lst2