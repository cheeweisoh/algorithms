class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """Minimum Distance Between BST Nodes

        Args:
            root (TreeNode): root of a Binary Search Tree (BST)

        Returns:
            ans (int): minimum difference between the values of any two different nodes in the tree
        """
        self.ans = float('inf')
        self.pred = None
        self.inorder(root)
        return self.ans

    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return
        
        self.inorder(root.left)
        if self.pred is not None:
            self.ans = min(self.ans, root.val - self.pred)
        self.pred = root.val
        self.inorder(root.right)