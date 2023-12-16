class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Maximum Depth of Binary Tree

        Args:
            root (TreeNode): root of binary tree

        Returns:
            int: maximum depth of the binary tree
        """
        if not root:
            return 0

        leftSubtree = self.maxDepth(root.left)
        RightSubtree = self.maxDepth(root.right)
        
        return max(leftSubtree, RightSubtree) + 1