class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Invert Binary Tree

        Args:
            root (TreeNode): root of binary tree

        Returns:
            root (TreeNode): root of inverted binary tree
        """
        if root == None:
            return
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root