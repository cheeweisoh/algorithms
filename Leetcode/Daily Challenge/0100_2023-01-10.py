class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Same Tree

        Args:
            p (TreeNode): root of first binary tree
            q (TreeNode): root of second binary tree

        Returns:
            (bool): true if both trees are the same, false otherwise
        """
        
        def helper(a: TreeNode, b: TreeNode) -> bool:
            if bool(a) ^ bool(b):
                return False
            else:
                if not bool(a):
                    return True
                elif a.val == b.val:
                    return helper(a.left, b.left) and helper(a.right, b.right)
                else:
                    return False
                
        return helper(p, q)