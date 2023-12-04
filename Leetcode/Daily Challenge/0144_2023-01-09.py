class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        """Binary Tree Preorder Traversal

        Args:
            root (TreeNode): root of a binary tree

        Returns:
            values: preorder traversal of its nodes' values
        """
        if not root:
            return []
        
        values = []
        
        def helper(node: TreeNode):
            values.append(node.val)
            
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
                
        helper(root)
        
        return values